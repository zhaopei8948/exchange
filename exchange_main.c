#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>
#include <ctype.h>
#include <wchar.h>
#include <locale.h>
#include <getopt.h>
#include <unistd.h>
#include <signal.h>
#include <pthread.h>
#include <uuid/uuid.h>
#include <cJSON.h>
#include "log/log.h"
#include "err/error.h"
#include "base64/base64.h"
#include "config/config.h"
#include "redis/redis_tool.h"

/* includes for MQ */
#include <cmqc.h>
#include <cmqxc.h>
#define BUFFER_SIZE 20000
#define MAX_PATH 200

/* private function declarations */
static void help(const char *restrict cmdName);
static int parseOption(int argc, char **argv);

typedef struct {
    MQBYTE *data;
    size_t size;
} MQMESSAGE;
MQMESSAGE *gBuffer;
int bufferCount = 0;
int loglevel = 0;
char configFile[MAX_PATH + 1] = "\0";

void startGetMessage();
void initalThread();
void stopApplication(int signum);
void messageConsumer(MQHCONN hConn, MQMD *pMsgDesc, MQGMO *pGetMsgOpts, MQBYTE *Buffer, MQCBC *pContext);
void writeMessageToFile(MQMESSAGE *message);

pthread_t *threads;
long nprocs = -1;

MQCHAR QMgrName[MQ_Q_MGR_NAME_LENGTH];   /* queue manager name            */
MQCNO   cno = {MQCNO_DEFAULT};                /* connection description        */
MQCD     cd = {MQCD_CLIENT_CONN_DEFAULT};     /* client connection description */
MQOD     od = {MQOD_DEFAULT};                 /* object description            */
MQMD     md = {MQMD_DEFAULT};                 /* message description           */
MQGMO   gmo = {MQGMO_DEFAULT};                /* get message options           */
MQCBD   cbd = {MQCBD_DEFAULT};                /* callback description          */
MQCTLO ctlo = {MQCTLO_DEFAULT};               /* control options               */

MQLONG o_options;             /* MQOPEN options                */
MQCHAR channelName[MQ_CHANNEL_NAME_LENGTH];
MQCHAR queueName[MQ_Q_NAME_LENGTH];
MQCHAR connectionName[MQ_CONN_NAME_LENGTH];
MQLONG ccsid = MQENC_NATIVE;
static char *PROJECT_NAME = "exchange";
static char *VERSION_NO = "1.0";
static pthread_mutex_t main_mutex = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t main_cond = PTHREAD_COND_INITIALIZER;  /* main condition variable */
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t condc = PTHREAD_COND_INITIALIZER;  /* consumer condition variable */
static pthread_cond_t condp = PTHREAD_COND_INITIALIZER;  /* producer condition variable */
static FILE *LOGFILE;
static char *logFileName = "exchange.log";

char backupPath[MAX_PATH] = "\0";

static void help(const char *restrict cmdName)
{
    printf("%s %s\n", PROJECT_NAME, VERSION_NO);
    printf("    -x --connname <Connection Name> Connection Name such as 192.168.1.1 or 192.168.1.1(2400)\n");
    printf("    -c --channelname <Channel Name> Server Connection channel(for use by clients)\n");
    printf("    -m --qmname <Queue Manager Name> Queue Manager Name\n");
    printf("    -q --queue <Queue Name> Queue Name local or remote\n");
    printf("    -d --ccsid <ccsid> ccsid\n");
    printf("    -b --backup <backup path> backup queue message\n");
    printf("    -l --loglevel <loglevel> log level, 0:TRACE(default), 1:DEBUG, 2:INFO, 3:WARN, 4:ERROR, 5:FATAL\n");
    printf("    -f --file <config file path> config file path\n");
    printf("    -H --hostname <redis host name> redis host name default 127.0.0.1\n");
    printf("    -p --port <redis port> redis port. default 6379\n");
    printf("    -h --help show help menu\n");
}

static int parseOption(int argc, char **argv)
{
    char *cmd = argv[0];
    int result = 0;
    if (argc == 1) {
        help(cmd);
        return -1;
    }
    int option_index = 0;
    struct option long_options[] = {
        {"connname",         required_argument, 0, 'x'},
        {"channelname",      required_argument, 0, 'c'},
        {"qmname",           required_argument, 0, 'm'},
        {"queue",            required_argument, 0, 'q'},
        {"ccsid",            required_argument, 0, 'd'},
        {"backup",           required_argument, 0, 'b'},
        {"loglevel",         required_argument, 0, 'l'},
        {"file",             required_argument, 0, 'f'},
        {"hostname",         required_argument, 0, 'H'},
        {"port",             required_argument, 0, 'p'},
        {"help",             no_argument,       0, 'h'}
    };
    while (1) {
        int c;

        c = getopt_long(argc, argv, "x:c:m:q:d:b:l:f:H:p:h", long_options, &option_index);
        if (c == -1)
            break;

        switch (c) {
        case 'x':
            strncpy(connectionName, optarg, MQ_CONN_NAME_LENGTH);
            log_info("ConnectionName is: %s", connectionName);
            break;
        case 'c':
            strncpy(channelName, optarg, MQ_CHANNEL_NAME_LENGTH);
            log_info("ChannelName is: %s", channelName);
            break;
        case 'm':
            strncpy(QMgrName, optarg, MQ_Q_MGR_NAME_LENGTH);
            log_info("QmgrName is: %s", QMgrName);
            break;
        case 'q':
            strncpy(queueName, optarg, MQ_Q_NAME_LENGTH);
            log_info("QueueName is: %s", queueName);
            break;
        case 'd':
            ccsid = atoi(optarg);
            log_info("ccsid is: %d", ccsid);
            break;
        case 'b':
            strncpy(backupPath, optarg, MAX_PATH);
            log_info("backupPath is: %s", backupPath);
            break;
        case 'l':
            loglevel = atoi(optarg);
            log_info("loglevel is: %d", loglevel);
            break;
        case 'f':
            strncpy(configFile, optarg, MAX_PATH);
            log_info("configFile is: %s", configFile);
            break;
        case 'H':
            strncpy(hostname, optarg, HOSTNAME_LENGTH);
            log_info("redis hostname is: %s", hostname);
            break;
        case 'p':
            port = atoi(optarg);
            log_info("redis port is: %d", port);
            break;
        default:
            help(cmd);
            result = -1;
            break;
        }
    }

    return result;
}

/********************************************************************/
/* FUNCTION: messageConsumer                                        */
/* PURPOSE : Callback function called when messages arrive          */
/********************************************************************/
void messageConsumer(MQHCONN   hConn,
        MQMD    * pMsgDesc,
        MQGMO   * pGetMsgOpts,
        MQBYTE  * Buffer,
        MQCBC   * pContext)
{
    MQLONG i,max;
    MQLONG length;
    pthread_t tid = pthread_self();

    switch(pContext->CallType)
    {
        case MQCBCT_MSG_REMOVED:
        case MQCBCT_MSG_NOT_REMOVED:
            length = pGetMsgOpts -> ReturnedLength;
            if (pContext->Reason)
                log_info("tid: %u Message Call (%d Bytes) : Reason = %d", (unsigned int)tid, length, pContext->Reason);
            else
                log_info("tid: %u Message Call (%d Bytes) :", (unsigned int)tid, length);

            pthread_mutex_lock(&mtx);
            while (bufferCount == BUFFER_SIZE)
                pthread_cond_wait(&condp, &mtx);

            gBuffer[bufferCount].size = length;
            gBuffer[bufferCount].data = (MQBYTE *) malloc(sizeof(MQBYTE) * (length + 1));
            memcpy(gBuffer[bufferCount].data, Buffer, length);
            gBuffer[bufferCount].data[length] = '\0';
            bufferCount++;

            if (bufferCount > 0)
                pthread_cond_signal(&condc);

            pthread_mutex_unlock(&mtx);
            break;

        case MQCBCT_EVENT_CALL:
            log_error("Event Call : Reason = %d",pContext->Reason);
            break;

        default:
            log_error("Calltype = %d",pContext->CallType);
            break;

    }
}

void stopApplication(int signum)
{
    int rtnVal = 1;
    if (threads != NULL) {
        for (int i = 0; i < nprocs; i++)
            pthread_cancel(threads[i]);
        free(threads);
    }

    if (gBuffer != NULL)
        free(gBuffer);

    log_debug("handle SIGINT signal");
    if (LOGFILE) {
        fclose(LOGFILE);
    }

    disconnectRedis();
    exit(0);
}

void startGetMessage()
{
    strncpy(cd.ConnectionName, connectionName, MQ_CONN_NAME_LENGTH);
    strncpy(cd.ChannelName, channelName, MQ_CHANNEL_NAME_LENGTH);
    strncpy(od.ObjectName, queueName, MQ_Q_NAME_LENGTH);

    cd.DefReconnect = MQRCN_YES;      /* client automatically reconnection */
    cno.Options |= MQCNO_RECONNECT;  /* reconnect */
    cno.ClientConnPtr = &cd;
    cno.Version = MQCNO_VERSION_2;   /* client connection set version 2 */

    cbd.CallbackFunction = messageConsumer;
    gmo.Options = MQGMO_NO_SYNCPOINT;

    o_options = MQOO_INPUT_AS_Q_DEF      /* open queue for input      */
              | MQOO_FAIL_IF_QUIESCING;  /* but not if MQM stopping   */

    MQHCONN hcon = MQHC_UNUSABLE_HCONN;
    MQHOBJ hobj;
    MQLONG compCode;
    MQLONG reasCode;

    MQCONNX(QMgrName,              /* queue manager          */
            &cno,                  /* connection options     */
            &hcon,                 /* connection handle      */
            &compCode,             /* completion code        */
            &reasCode);            /* reason code            */

    if (compCode == MQCC_FAILED) {
        log_error("MQCONNX ended with reason code %d", reasCode);
        exit(reasCode);
    }

    MQOPEN(hcon,                    /* connection handle            */
           &od,                     /* object descriptor for queue  */
           o_options,               /* open options                 */
           &hobj,                   /* object handle                */
           &compCode,               /* completion code              */
           &reasCode);              /* reason code                  */

    if (compCode == MQCC_FAILED) {
        log_error("MQOPEN of '%.48s' ended with reason code %d",
                &od.ObjectName, reasCode);
        exit(reasCode);
    }

    /****************************************************************/
    /*                                                              */
    /*   Register a consumer                                        */
    /*                                                              */
    /****************************************************************/

    md.Encoding = ccsid;
    MQCB(hcon,
            MQOP_REGISTER,
            &cbd,
            hobj,
            &md,
            &gmo,
            &compCode,
            &reasCode);
    if (compCode == MQCC_FAILED) {
        log_error("MQCB ended with reason code %d", reasCode);
        exit(reasCode);
    }

    /******************************************************************/
    /*                                                                */
    /*  Start consumption of messages                                 */
    /*                                                                */
    /******************************************************************/
    MQCTL(hcon,
            MQOP_START,
            &ctlo,
            &compCode,
            &reasCode);
    if (compCode == MQCC_FAILED) {
        log_error("MQCTL ended with reason code %d", reasCode);
        exit(reasCode);
    }
}

void *workThread(void *arg)
{
    pthread_t tid = pthread_self();
    MQMESSAGE message;
    while (1) {
        pthread_mutex_lock(&mtx);
        while (bufferCount <= 0)
            pthread_cond_wait(&condc, &mtx);

        message = gBuffer[--bufferCount];

        if (bufferCount <= 0)
            pthread_cond_signal(&condp);

        pthread_mutex_unlock(&mtx);
        log_info("workThread: %u, message (%u Bytes) :", (unsigned int)tid, message.size);

        if (message.data != NULL) {
            log_info("thread: %u, message is: [%s]", (unsigned int)tid, message.data);
            if (strlen(backupPath) > 0)
                writeMessageToFile(&message);
            free(message.data);
        } else {
            log_info("thread: %u, no data.", (unsigned int)tid);
        }
        message.size = 0;
    }
}

char *mergePath(char *dstpath, const char *filePrefix, const char *uuid, const char *fileExt)
{
    strcat(dstpath, "/");
    strcat(dstpath, filePrefix);
    strcat(dstpath, uuid);
    strcat(dstpath, fileExt);
    return dstpath;
}

int notExistsCreateDir(const char *dir)
{
    if (access(dir, R_OK) != 0) {
        if (mkdir(dir, 0755) == -1) {
            log_error("mkdir %s error.", dir);
            return -1;
        }
    }

    return 0;
}

void writeMessageToFile(MQMESSAGE *message)
{
    uuid_t uuid;
    char uuidStr[36];
    char *filePrefix = "FILE_BACKUP_";
    char *tmpFileExt = ".writing";
    char *fileExt = ".xml";
    char tmpFilePath[MAX_PATH];
    char filePath[MAX_PATH];
    FILE *tmpfp;

    uuid_generate(uuid);
    uuid_unparse(uuid, uuidStr);
    pthread_t tid = pthread_self();

    if (notExistsCreateDir(backupPath) == -1)
        return;

    strcpy(tmpFilePath, backupPath);
    strcpy(filePath, backupPath);

    mergePath(tmpFilePath, filePrefix, uuidStr, tmpFileExt);
    mergePath(filePath, filePrefix, uuidStr, fileExt);
    log_info("thread: %u, tmpFilePath: %s, filePath: %s", (unsigned int)tid, tmpFilePath, filePath);

    tmpfp = fopen(tmpFilePath, "w");
    if (tmpfp == NULL) {
        log_error("fopen error.");
        return;
    }

    char *dataStart = "<Data>";
    char *dataEnd = "</Data>";

    char *dataStartPos = strstr(message->data, "<Data>");
    char *dataEndPos = strstr(message->data, "</Data>");

    if (dataStartPos && dataEndPos && dataEndPos > dataStartPos) {
        *dataEndPos = '\0';
        setlocale(LC_ALL, "en_US.utf8");
        size_t dataLength = (dataEndPos - dataStartPos) * 3 / 4;
        char *startPos = dataStartPos + strlen(dataStart);
        log_info("data is %s", startPos);
        char *odata = (char *)malloc(sizeof(char) * dataLength);
        size_t bytes = base64_decode(startPos, odata);
        odata[bytes] = '\0';
        log_info("bytes is %u", bytes);
        log_info("odata is %s", odata);
        fprintf(tmpfp, "%s", odata);
        free(odata);
    } else {
        for (int i = 0; i < message->size; i++)
            fputc(message->data[i], tmpfp);
    }

    fclose(tmpfp);

    if (rename(tmpFilePath, filePath) == -1)
        log_error("thread: %u, rename error.", (unsigned int)tid);
    else
        log_info("thread: %u, rename %s -> %s success.", (unsigned int)tid, tmpFilePath, filePath);
}

void initalThread()
{
    log_info("nprocs is %d", nprocs);
    threads = (pthread_t *) malloc(sizeof(pthread_t) * nprocs);
    for (int i = 0; i < nprocs; i++) {
        pthread_create(threads + i, NULL, workThread, NULL);
    }
}

int main(int argc, char **argv)
{
    LOGFILE = fopen(logFileName, "a");
    if (!LOGFILE) {
            LOGFILE = fopen(logFileName, "w");
            if (!LOGFILE) {
                err_sys("File opening failed");
            }

    }
    log_set_fp(LOGFILE);

    if (parseOption(argc, argv) < 0) {
        exit(1);
    }
    log_set_level(loglevel);

    if (strlen(configFile) > 0) {
        parseConfig(configFile);
        log_error("config file content: ");
        log_error("defaultTarget qmId: %d", defaultTarget.qmId);
        log_error("defaultTarget queue: %s", defaultTarget.queue);
        log_error("queueManagerSize is: %d", queueManagerSize);
        for (int i = 0; i < queueManagerSize; i++) {
            log_error("[%d] queueManager qmId: %d", i, queueManagers[i].qmId);
            log_error("[%d] queueManager hostName: %s", i, queueManagers[i].hostName);
            log_error("[%d] queueManager port: %d", i, queueManagers[i].port);
            log_error("[%d] queueManager queueManager: %s", i, queueManagers[i].queueManager);
            log_error("[%d] queueManager channel: %s", i, queueManagers[i].channel);
            log_error("[%d] queueManager ccsid: %d", i, queueManagers[i].ccsid);
        }

        log_error("dxpIdDistributionSize is: %d", dxpIdDistributionSize);
        for (int i = 0; i < dxpIdDistributionSize; i++) {
            log_error("[%d] dxpIdDistribution dxpId: %s", i, dxpIdDistributions[i].dxpId);
            log_error("[%d] dxpIdDistribution qmId: %d", i, dxpIdDistributions[i].qmId);
            log_error("[%d] dxpIdDistribution queue: %s", i, dxpIdDistributions[i].queue);
        }
    }

    nprocs = sysconf(_SC_NPROCESSORS_ONLN);
    if (nprocs == -1) {
        log_info("get processors error.");
        exit(1);
    }

    signal(SIGINT, stopApplication);
    signal(SIGQUIT, stopApplication);

    gBuffer = (MQMESSAGE *) malloc(sizeof(MQMESSAGE) * BUFFER_SIZE);
    initConnectionRedis();
    initalThread();
    startGetMessage();
    /* while (1); */
    pthread_mutex_lock(&main_mutex);
    pthread_cond_wait(&main_cond, &main_mutex);
    pthread_mutex_unlock(&main_mutex);

    stopApplication(SIGINT);

    exit(0);
}

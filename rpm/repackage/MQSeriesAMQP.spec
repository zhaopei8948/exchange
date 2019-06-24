Summary: IBM MQ AMQP Service
Name: MQSeriesAMQP
Version: 9.0.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesJava >= 8.0.0-0
Requires: MQSeriesJRE >= 8.0.0-0
Requires: MQSeriesServer >= 8.0.0-0
Requires: MQSeriesRuntime >= 8.0.0-0
%define _source_filedigest_algorithm md5
%define _binary_filedigest_algorithm md5
%define _source_payload w7.lzdio
%define _binary_payload w7.lzdio
%global __strip /bin/true
%global _rpmdir /build/slot2/p900_P/inst.images/amd64_linux_2/images/
%global _tmppath /build/slot2/p900_P/obj/amd64_linux_2/install/unix/linux_2
BuildRoot: /build/slot2/p900_P/obj/amd64_linux_2/ship

%description
IBM MQ for Developers for Linux for x86_64 
5724-H72 
This package adds support for the IBM MQ AMQP Service.

%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/amqp
install -d $RPM_BUILD_ROOT/opt/mqm/amqp/bin
install -d $RPM_BUILD_ROOT/opt/mqm/amqp/config
install -d $RPM_BUILD_ROOT/opt/mqm/amqp/lib
install -d $RPM_BUILD_ROOT/opt/mqm/amqp/samples
install -d $RPM_BUILD_ROOT/opt/mqm/amqp/samples/samples
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_AMQP_Service-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_AMQP_Service-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqsde $RPM_BUILD_ROOT/opt/mqm/bin/endmqsde
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/bin/controlAMQPChannel.sh $RPM_BUILD_ROOT/opt/mqm/amqp/bin/controlAMQPChannel.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/bin/controlAMQP_mqm.sh $RPM_BUILD_ROOT/opt/mqm/amqp/bin/controlAMQP_mqm.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/lib/com.ibm.mq.amqp.utils.jar $RPM_BUILD_ROOT/opt/mqm/amqp/lib/com.ibm.mq.amqp.utils.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/lib/objectManager.utils.jar $RPM_BUILD_ROOT/opt/mqm/amqp/lib/objectManager.utils.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/lib/com.ibm.mq.amqp.misc.jar $RPM_BUILD_ROOT/opt/mqm/amqp/lib/com.ibm.mq.amqp.misc.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/lib/AMQPListener.jar $RPM_BUILD_ROOT/opt/mqm/amqp/lib/AMQPListener.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/lib/nonBlockingTrace.jar $RPM_BUILD_ROOT/opt/mqm/amqp/lib/nonBlockingTrace.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/samples/CleanupMQM.sh $RPM_BUILD_ROOT/opt/mqm/amqp/samples/CleanupMQM.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/samples/SampleMQM.sh $RPM_BUILD_ROOT/opt/mqm/amqp/samples/SampleMQM.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/samples/samples/JAASLoginModule.class $RPM_BUILD_ROOT/opt/mqm/amqp/samples/samples/JAASLoginModule.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/samples/samples/JAASPrincipal.class $RPM_BUILD_ROOT/opt/mqm/amqp/samples/samples/JAASPrincipal.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/samples/samples/JAASPrincipal.java $RPM_BUILD_ROOT/opt/mqm/amqp/samples/samples/JAASPrincipal.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/samples/samples/JAASLoginModule.java $RPM_BUILD_ROOT/opt/mqm/amqp/samples/samples/JAASLoginModule.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/config/amqptraceOn.properties $RPM_BUILD_ROOT/opt/mqm/amqp/config/amqptraceOn.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/config/jaas.config $RPM_BUILD_ROOT/opt/mqm/amqp/config/jaas.config
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/config/amqptraceOff.properties $RPM_BUILD_ROOT/opt/mqm/amqp/config/amqptraceOff.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/config/amqp_unix.properties $RPM_BUILD_ROOT/opt/mqm/amqp/config/amqp_unix.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/config/amqp_trace.config $RPM_BUILD_ROOT/opt/mqm/amqp/config/amqp_trace.config
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/amqp/config/amqp_java.properties $RPM_BUILD_ROOT/opt/mqm/amqp/config/amqp_java.properties

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/amqp"
%dir %attr(555,mqm,mqm) "/opt/mqm/amqp/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/amqp/config"
%dir %attr(555,mqm,mqm) "/opt/mqm/amqp/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/amqp/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/amqp/samples/samples"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_AMQP_Service-9.0.0.mqtag"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqsde"
%attr(550,mqm,mqm) "/opt/mqm/amqp/bin/controlAMQPChannel.sh"
%attr(550,mqm,mqm) "/opt/mqm/amqp/bin/controlAMQP_mqm.sh"
%attr(444,mqm,mqm) "/opt/mqm/amqp/lib/com.ibm.mq.amqp.utils.jar"
%attr(444,mqm,mqm) "/opt/mqm/amqp/lib/objectManager.utils.jar"
%attr(444,mqm,mqm) "/opt/mqm/amqp/lib/com.ibm.mq.amqp.misc.jar"
%attr(444,mqm,mqm) "/opt/mqm/amqp/lib/AMQPListener.jar"
%attr(444,mqm,mqm) "/opt/mqm/amqp/lib/nonBlockingTrace.jar"
%attr(550,mqm,mqm) "/opt/mqm/amqp/samples/CleanupMQM.sh"
%attr(550,mqm,mqm) "/opt/mqm/amqp/samples/SampleMQM.sh"
%attr(444,mqm,mqm) "/opt/mqm/amqp/samples/samples/JAASLoginModule.class"
%attr(444,mqm,mqm) "/opt/mqm/amqp/samples/samples/JAASPrincipal.class"
%attr(444,mqm,mqm) "/opt/mqm/amqp/samples/samples/JAASPrincipal.java"
%attr(444,mqm,mqm) "/opt/mqm/amqp/samples/samples/JAASLoginModule.java"
%attr(444,mqm,mqm) "/opt/mqm/amqp/config/amqptraceOn.properties"
%attr(444,mqm,mqm) "/opt/mqm/amqp/config/jaas.config"
%attr(444,mqm,mqm) "/opt/mqm/amqp/config/amqptraceOff.properties"
%attr(444,mqm,mqm) "/opt/mqm/amqp/config/amqp_unix.properties"
%attr(444,mqm,mqm) "/opt/mqm/amqp/config/amqp_trace.config"
%attr(444,mqm,mqm) "/opt/mqm/amqp/config/amqp_java.properties"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ AMQP Service"
RPM_PACKAGE_NAME="MQSeriesAMQP"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/preinstall.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2016" 
#   crc="3530070126" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2005, 2016 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# 
# Common Preinstallation script for all packages
# 
# Check that this package is not being installed to a location where 
# a different VR exists
# 
#######################################################################################################
# Check the install path does not exceed the MQ maximum length of 256
#######################################################################################################
if [ ${#MQ_INSTALLATION_PATH} -gt 256 ]; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) exceeds MQ maximum length of 256"
  echo ""
  exit 1
fi

#######################################################################################################
# Check the install path does not contain unsupported charaters
#######################################################################################################
echo "${MQ_INSTALLATION_PATH}" | grep "[:%# ]" > /dev/null
if [ $? -eq 0 ] ; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character"
  echo ""
  exit 1
fi
# Trailing blanks 
echo "${MQ_INSTALLATION_PATH}" | grep "\ $" > /dev/null
if [ $? -eq 0 ] ; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character"
  echo ""
  exit 1
fi


#######################################################################################################
# Runtime checks
#######################################################################################################
echo ${RPM_PACKAGE_NAME} | grep  "MQSeriesRuntime" > /dev/null
if [ $? -eq 0 ] ; then
  #####################################################################################################
  # Check that the install path is empty 
  # ignore lost+found and .snapshots(GPFS) directories
  # The .snapshots directory can also be renamed within GPFS, so we allow an alternate name to be specified with
  # AMQ_IGNORE_SNAPDIRNAME
  #####################################################################################################
  if [ x${AMQ_OVERRIDE_EMPTY_INSTALL_PATH} = x ] ;then 
    if [ -d ${MQ_INSTALLATION_PATH} ] && [ ${MQ_INSTALLATION_PATH} != ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then
      if [ "${AMQ_IGNORE_SNAPDIRNAME}" = "" ] ; then
        SNAPDIR_NAME=".snapshots"
      else
        SNAPDIR_NAME="${AMQ_IGNORE_SNAPDIRNAME}"
      fi
      LS_ALL=`ls -A ${MQ_INSTALLATION_PATH} 2>/dev/null | grep -F -v "lost+found" | grep -F -v "${SNAPDIR_NAME}"`
      if [ "${LS_ALL}" ] ; then
        echo ""
        echo "ERROR:   Specified installation path '${MQ_INSTALLATION_PATH}' is not empty"
        echo ""
        exit 1
     fi
    fi
  fi
#######################################################################################################
# Non Runtime checks
#######################################################################################################
else
  #####################################################################################################
  # Check the version/release of the product already at MQ_INSTALLATION_PATH is the same as this one
  #####################################################################################################
  if [ -x ${MQ_INSTALLATION_PATH}/bin/dspmqver ] ; then
    INSTALLED_VR=$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b | awk -F. '{print $1 "." $2}')
    PACKAGE_VR=`echo ${RPM_PACKAGE_VERSION} | awk -F. '{print $1 "." $2}'`
    if [ ${INSTALLED_VR} != ${PACKAGE_VR} ] ; then
      echo ""
      echo "ERROR:   This package is not applicable to the MQ installation at ${MQ_INSTALLATION_PATH}"
      echo ""
      exit 1
    fi
  else
    echo ""
    echo "ERROR:   There is no MQSeriesRuntime installed at ${MQ_INSTALLATION_PATH}"
    echo ""
    exit 1
  fi
fi

#######################################################################################################
# Preventing an installation over an existing installation
# Each component has a unique '.cmptag' file.  If this is already present on the filesystem at the
# installation location, then the component must already be installed to this location, so we should
# abort.
#######################################################################################################
case "${RPM_PACKAGE_NAME}" in
  MQSeriesAMS)
      compfile="IBM_WebSphere_MQ_Advanced_Message_Security_Component."
      ;;
  MQSeriesASOAP)
      compfile="DOES_NOT_CONTAIN_A_COMPONENT_FILE"
      ;;
  MQSeriesAMQP)
      compfile="DOES_NOT_CONTAIN_A_COMPONENT_FILE"
      ;;
  MQSeriesClient)
      compfile="IBM_WebSphere_MQ_Client."
      ;;
  MQSeriesExplorer)
      compfile="IBM_WebSphere_MQ_Explorer."
      ;;
  MQSeriesFTAgent)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Agent."
      ;;
  MQSeriesFTBase)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Base."
      ;;
  MQSeriesFTLogger)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Logger."
      ;;
  MQSeriesFTService)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Service."
      ;;
  MQSeriesFTTools)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Tools."
      ;;
  MQSeriesGSKit)
      compfile='IBM_WebSphere_MQ_GSKit.'
      ;;
  MQSeriesJava)
      compfile="IBM_WebSphere_MQ_Java_Messaging."
      ;;
  MQSeriesJRE)
      compfile="IBM_WebSphere_MQ_JRE"
      ;;
  MQSeriesMan)
      compfile="IBM_WebSphere_MQ_Man_Pages."
      ;;
  MQSeriesMsg_cs)
      compfile="IBM_WebSphere_MQ_Messages_Czech."
      ;;
  MQSeriesMsg_de)
      compfile="IBM_WebSphere_MQ_Messages_German."
      ;;
  MQSeriesMsg_es)
      compfile="IBM_WebSphere_MQ_Messages_Spanish."
      ;;
  MQSeriesMsg_fr)
      compfile="IBM_WebSphere_MQ_Messages_French."
      ;;
  MQSeriesMsg_hu)
      compfile="IBM_WebSphere_MQ_Messages_Hungarian."
      ;;
  MQSeriesMsg_it)
      compfile="IBM_WebSphere_MQ_Messages_Italian."
      ;;
  MQSeriesMsg_ja)
      compfile="IBM_WebSphere_MQ_Messages_Japanese."
      ;;
  MQSeriesMsg_ko)
      compfile="IBM_WebSphere_MQ_Messages_Korean."
      ;;
  MQSeriesMsg_pl)
      compfile="IBM_WebSphere_MQ_Messages_Polish."
      ;;
  MQSeriesMsg_pt)
      compfile="IBM_WebSphere_MQ_Messages_Brazilian_Portuguese."
      ;;
  MQSeriesMsg_ru)
      compfile="IBM_WebSphere_MQ_Messages_Russian."
      ;;
  MQSeriesMsg_Zh_CN)
      compfile="IBM_WebSphere_MQ_Messages_Chinese_Simplified."
      ;;
  MQSeriesMsg_Zh_TW)
      compfile="IBM_WebSphere_MQ_Messages_Chinese_Traditional."
      ;;
  MQSeriesRuntime)
      compfile="IBM_WebSphere_MQ_Runtime."
      ;;
  MQSeriesSamples)
      compfile="IBM_WebSphere_MQ_Samples."
      ;;
  MQSeriesSDK)
      compfile="IBM_WebSphere_MQ_SDK."
      ;;
  MQSeriesServer)
      compfile="IBM_WebSphere_MQ_Server."
      ;;
  MQSeriesXRService)
      compfile="IBM_WebSphere_MQ_Telemetry_Service."
      ;;
  *)
      echo "ERROR: Package name ${RPM_PACKAGE_NAME} not recognised, aborting installation."
      exit 1
      ;;
esac

# RPM_PACKAGE_VERSION is of the form 8.0.0
# If the 'compfile' file is present, then the package is already installed on
# the system, and we abort the installation of this package.
# NOTE the careful positioning of the wildcard outside the doublequotes.
if [ -f "${MQ_INSTALLATION_PATH}/properties/version/${compfile}"* ]; then
  echo "ERROR:  The specified installation path (${MQ_INSTALLATION_PATH}) already"
  echo "        has this package (${RPM_PACKAGE_NAME}) installed."
  echo "        Aborting installation."
  exit 1
fi

#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="1114153681" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# Preinstallation script
# Check's to see if the license agreement has been accepted

if [ ! -r /tmp/mq_license_${RPM_PACKAGE_VERSION}/license/status.dat ] && [ ! -r "${MQ_INSTALLATION_PATH}/licenses/status.dat" ] ; then

    cat << +++EOM+++
ERROR:  Product cannot be installed until the license
        agreement has been accepted.
        Run the 'mqlicense' script, which is in the root
        directory of the install media, or see the
        installation instructions in the product 
        Infocenter for more information
+++EOM+++

   exit 1
fi

  #####################################################################################################
  # Check the version/release of the product already at MQ_INSTALLATION_PATH is the same as this package
  #####################################################################################################
  if [ -x ${MQ_INSTALLATION_PATH}/bin/dspmqver ] ; then
    INSTALLED_VRMF=$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b )
    PACKAGE_VRMF=`echo  ${RPM_PACKAGE_VERSION}.${RPM_PACKAGE_RELEASE}`
    if [ ${INSTALLED_VRMF} != ${PACKAGE_VRMF} ] ; then
      echo ""
      echo "ERROR:   This package is not applicable to the WebSphere MQ installation at ${MQ_INSTALLATION_PATH}"
      echo ""
      exit 1
    fi
  else
    echo ""
    echo "ERROR:   There is no MQSeriesRuntime installed at ${MQ_INSTALLATION_PATH}"
    echo ""
    exit 1
  fi
echo > /dev/null 2>/dev/null

%post
RPM_PACKAGE_SUMMARY="IBM MQ AMQP Service"
RPM_PACKAGE_NAME="MQSeriesAMQP"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi
if [ ${MQ_INSTALLATION_PATH} !=  ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then 
  if [ -x ${MQ_INSTALLATION_PATH}/bin/amqicrel ] ; then 
     ${MQ_RUNSCRIPT} ${MQ_INSTALLATION_PATH}/bin/amqicrel ${MQ_INSTALLATION_PATH} ${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
  fi
fi

%preun
RPM_PACKAGE_SUMMARY="IBM MQ AMQP Service"
RPM_PACKAGE_NAME="MQSeriesAMQP"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2016" 
#   crc="122768040" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2005, 2016 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre-uninstallation script
# Checks for already running Q Managers, and if it finds one, stops the
# uninstall.

# If amqiclen exists (should do during uninstall) then run it to clean up
# IPCC resources. If amqiclen returns an error then a queue manager is still
# running so stop the uninstall.
if [ -x ${MQ_INSTALLATION_PATH}/bin/amqiclen ] && [ -f /var/mqm/mqs.ini ]
then
    ${MQ_INSTALLATION_PATH}/bin/amqiclen -v -x > /tmp/amqiclen.$$.out 2>&1
    amqiclen_rc=$?
    if [ $amqiclen_rc -ne 0 ] 
    then
        echo " " >&2
        echo "ERROR: MQ shared resources associated with the installation at" >&2
        echo "      '${MQ_INSTALLATION_PATH}' are still in use." >&2
        echo "       You must stop all MQ processing, including applications, Queue Managers" >&2 
        echo "       and Listeners before attempting to install, update or delete" >&2
        echo "       the MQ product." >&2
        echo " " >&2
        echo "       'amqiclen -v -x' return code was: '$amqiclen_rc', output was:" >&2
        cat /tmp/amqiclen.$$.out >&2
        echo " " >&2
        rm -f /tmp/amqiclen.$$.out
        exit 1
    fi
    rm -f /tmp/amqiclen.$$.out
fi 
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="1595222582" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre-uninstallation check script for all components
# A check is performed to see if there are any fixpack filesets applied to
# the base component which is currently being uninstalled.  If the fixpack
# has been applied, the uninstallation of this component is aborted to prevent
# the situation where the base fileset has been uninstalled leaving an
# uninstallable fixpack.

FIXPACK_BACKUPDIR="${MQ_INSTALLATION_PATH}/maintenance"

unset fix_exists

fix_exists=$(find $FIXPACK_BACKUPDIR -type d -maxdepth 2 -print 2>/dev/null | \
while read directory ; do
  component=`basename $directory`
  if [ "$RPM_PACKAGE_NAME" = "$component" ]; then
    # safety check - are there actually files under this directory?
    num_files=`find "$directory" -type f -print 2>/dev/null | wc -l`
    if [ $num_files -gt 0 ]; then
      echo  $num_files
      exit
    fi
  fi
done
)
if [ ! -z $fix_exists ] ; then 
  echo "ERROR:  There appears to be a fixpack installed on this machine for this" >&2
  echo "        component." >&2
  echo "" >&2
  echo "        Please ensure you have removed all fixpacks for the ${RPM_PACKAGE_NAME}" >&2
  echo "        component before trying to remove this package." >&2
  echo "" >&2
  exit 1 
fi
# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/amqp_preuninstall.sh
#
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2015" 
#   crc="598641773" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2005, 2015 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre uninstallation script

# Removes the amqp license text files

rm -rf ${MQ_INSTALLATION_PATH}/amqp/licenses/.amqp-license

echo "Resetting return code to success" > /dev/null

# Removing product links

%postun
RPM_PACKAGE_SUMMARY="IBM MQ AMQP Service"
RPM_PACKAGE_NAME="MQSeriesAMQP"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi


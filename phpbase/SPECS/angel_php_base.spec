%define base_dir /usr/local/angel.com
%define config_dest_dir /usr/local/angel.com/builds/call-server/1
Name: angel_call_server
Version: 105
Release: 105
Summary: Angel Jboss Server
License: 2009, Angel.com
Distribution: Angel System Config
Group: Angel.Com Engineering
Requires: angel_core
Requires: angel_environment
Requires: angel_call_deploy
Requires: angel_jboss_43CP04
autoprov: yes
autoreq: yes
Prefix: /usr/local
BuildRoot: /var/lib/hudson/jobs/call-server/workspace/default/angel-server-assembly/target/rpm/angel_call_server/buildroot

%description
Used to create jboss server distributions.  If you want one as a zip, use the command mvn -Dservice=[sb|reporting} assembly:assembly

%files
%defattr(644,jbrunner,jbrunner,755)
%dir  /var/log/angel/jboss-call
%dir  /usr/local/angel.com/builds/call-server
%dir  /usr/local/angel.com/builds/call-server/1
%dir %attr(755,jbrunner,jbrunner) /usr/local/angel.com/jboss-versions/jboss-eap-4.3.0.GA_CP04/jboss-as/bin
%attr(755,jbrunner,jbrunner) /usr/local/angel.com/jboss-versions/jboss-eap-4.3.0.GA_CP04/jboss-as/bin/startAngel-call.sh
%config(noreplace)  /usr/local/angel.com/jboss-versions/jboss-eap-4.3.0.GA_CP04/jboss-as/bin/call.conf
%config(noreplace)  /usr/local/angel.com/builds/call-server/1/jboss-log4j.xml
%config(noreplace)  /usr/local/angel.com/builds/call-server/1/run.conf
 /usr/local/angel.com/builds/call-server/1/conf/jndi.properties
 /usr/local/angel.com/builds/call-server/1/conf/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/conf/login-config.xml
 /usr/local/angel.com/builds/call-server/1/conf/jboss-minimal.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/AttributePersistenceService-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/TransactionManagerService-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/NamingService-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/org.jboss.deployment.SARDeployer-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/JNDIView-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/Log4jService-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/org.jboss.deployment.JARDeployer-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/org.jboss.deployment.MainDeployer-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/NamingBean-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/xmdesc/ClientUserTransaction-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/conf/standardjbosscmp-jdbc.xml
 /usr/local/angel.com/builds/call-server/1/conf/standardjboss.xml
 /usr/local/angel.com/builds/call-server/1/conf/jacorb.properties
 /usr/local/angel.com/builds/call-server/1/conf/jbossjta-properties.xml
 /usr/local/angel.com/builds/call-server/1/conf/jboss-log4j.xml
 /usr/local/angel.com/builds/call-server/1/conf/props/jmx-console-roles.properties
 /usr/local/angel.com/builds/call-server/1/conf/props/jbossws-roles.properties
 /usr/local/angel.com/builds/call-server/1/conf/props/jbossws-users.properties
 /usr/local/angel.com/builds/call-server/1/conf/props/jmx-console-users.properties
 /usr/local/angel.com/builds/call-server/1/farm/cluster-examples-service.xml
 /usr/local/angel.com/builds/call-server/1/lib/jboss-jaxrpc.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-cache-jdk50.jar
 /usr/local/angel.com/builds/call-server/1/lib/properties-plugin.jar
 /usr/local/angel.com/builds/call-server/1/lib/scheduler-plugin.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-jaxws.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-ejb3x.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-hibernate.jar
 /usr/local/angel.com/builds/call-server/1/lib/hibernate-commons-annotations.jar
 /usr/local/angel.com/builds/call-server/1/lib/bindingservice-plugin.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-management.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-vfs.jar
 /usr/local/angel.com/builds/call-server/1/lib/hibernate-entitymanager.jar
 /usr/local/angel.com/builds/call-server/1/lib/jmx-adaptor-plugin.jar
 /usr/local/angel.com/builds/call-server/1/lib/jgroups.jar
 /usr/local/angel.com/builds/call-server/1/lib/joesnmp.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-monitoring.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-srp.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-jsr88.jar
 /usr/local/angel.com/builds/call-server/1/lib/bsf.jar
 /usr/local/angel.com/builds/call-server/1/lib/asm-attrs.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-iiop.jar
 /usr/local/angel.com/builds/call-server/1/lib/antlr.jar
 /usr/local/angel.com/builds/call-server/1/lib/mail-plugin.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossws-spi.jar
 /usr/local/angel.com/builds/call-server/1/lib/jacorb.jar
 /usr/local/angel.com/builds/call-server/1/lib/hsqldb-plugin.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-remoting-int.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossws-jboss42.jar
 /usr/local/angel.com/builds/call-server/1/lib/msutil.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossws-common.jar
 /usr/local/angel.com/builds/call-server/1/lib/slf4j-log4j12-1.5.6.jar
 /usr/local/angel.com/builds/call-server/1/lib/mssqlserver.jar
 /usr/local/angel.com/builds/call-server/1/lib/servlet-api.jar
 /usr/local/angel.com/builds/call-server/1/lib/jnpserver.jar
 /usr/local/angel.com/builds/call-server/1/lib/activation.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-transaction.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbosssx.jar
 /usr/local/angel.com/builds/call-server/1/lib/hibernate-validator.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossts-common.jar
 /usr/local/angel.com/builds/call-server/1/lib/commons-codec.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossjta-integration.jar
 /usr/local/angel.com/builds/call-server/1/lib/scheduler-plugin-example.jar
 /usr/local/angel.com/builds/call-server/1/lib/bsh-deployer.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss.jar
 /usr/local/angel.com/builds/call-server/1/lib/el-api.jar
 /usr/local/angel.com/builds/call-server/1/lib/commons-logging.jar
 /usr/local/angel.com/builds/call-server/1/lib/jsp-api.jar
 /usr/local/angel.com/builds/call-server/1/lib/bsh.jar
 /usr/local/angel.com/builds/call-server/1/lib/jaxen.jar
 /usr/local/angel.com/builds/call-server/1/lib/msbase.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-jsr77.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-j2ee.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-messaging-client.jar
 /usr/local/angel.com/builds/call-server/1/lib/xmlentitymgr.jar
 /usr/local/angel.com/builds/call-server/1/lib/log4j.jar
 /usr/local/angel.com/builds/call-server/1/lib/mysql.jar
 /usr/local/angel.com/builds/call-server/1/lib/httpunit.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossjta.jar
 /usr/local/angel.com/builds/call-server/1/lib/slf4j-api-1.5.8.jar
 /usr/local/angel.com/builds/call-server/1/lib/cglib.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossha.jar
 /usr/local/angel.com/builds/call-server/1/lib/commons-httpclient.jar
 /usr/local/angel.com/builds/call-server/1/lib/bcel.jar
 /usr/local/angel.com/builds/call-server/1/lib/mail.jar
 /usr/local/angel.com/builds/call-server/1/lib/ejb3-persistence.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-saaj.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-messaging.jar
 /usr/local/angel.com/builds/call-server/1/lib/hibernate3.jar
 /usr/local/angel.com/builds/call-server/1/lib/avalon-framework.jar
 /usr/local/angel.com/builds/call-server/1/lib/log4j-snmp-appender.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-remoting.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-common-jdbc-wrapper.jar
 /usr/local/angel.com/builds/call-server/1/lib/jtds-0.9.1.jar
 /usr/local/angel.com/builds/call-server/1/lib/hsqldb.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-jca.jar
 /usr/local/angel.com/builds/call-server/1/lib/dom4j.jar
 /usr/local/angel.com/builds/call-server/1/lib/jboss-serialization.jar
 /usr/local/angel.com/builds/call-server/1/lib/ojdbc14-10.2.jar
 /usr/local/angel.com/builds/call-server/1/lib/jbossws-framework.jar
 /usr/local/angel.com/builds/call-server/1/lib/asm.jar
 /usr/local/angel.com/builds/call-server/1/lib/javassist.jar
 /usr/local/angel.com/builds/call-server/1/lib/hibernate-annotations.jar
 /usr/local/angel.com/builds/call-server/1/lib/commons-collections.jar
 /usr/local/angel.com/builds/call-server/1/lib/autonumber-plugin.jar
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi-saaj.jar
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/scout.jar
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi.war/styles.css
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi.war/index.html
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi.war/WEB-INF/jboss-web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi.war/WEB-INF/web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi.war/WEB-INF/classes/org/jboss/jaxr/juddi/JUDDIServlet.class
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi.war/WEB-INF/juddi.properties
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi-service.jar
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/juddi.jar
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/META-INF/MANIFEST.MF
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/META-INF/ddl/juddi_create_db.ddl
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/META-INF/ddl/juddi_data.ddl
 /usr/local/angel.com/builds/call-server/1/deploy/juddi-service.sar/META-INF/ddl/juddi_drop_db.ddl
 /usr/local/angel.com/builds/call-server/1/deploy/scheduler-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/iiop-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/monitoring-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-ha-xa-jdbc.rar
 /usr/local/angel.com/builds/call-server/1/deploy/snmp-adaptor.sar/notifications.xml
 /usr/local/angel.com/builds/call-server/1/deploy/snmp-adaptor.sar/snmp-adaptor.jar
 /usr/local/angel.com/builds/call-server/1/deploy/snmp-adaptor.sar/managers.xml
 /usr/local/angel.com/builds/call-server/1/deploy/snmp-adaptor.sar/attributes.xml
 /usr/local/angel.com/builds/call-server/1/deploy/snmp-adaptor.sar/attributes.mib
 /usr/local/angel.com/builds/call-server/1/deploy/snmp-adaptor.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/snmp-adaptor.sar/META-INF/MANIFEST.MF
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/invoker.war/WEB-INF/jboss-web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/invoker.war/WEB-INF/web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/invoker.war/WEB-INF/classes/org/jboss/invocation/http/servlet/ReadOnlyAccessFilter.class
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/invoker.war/WEB-INF/classes/org/jboss/invocation/http/servlet/InvokerServlet.class
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/invoker.war/WEB-INF/classes/org/jboss/invocation/http/servlet/InvokerServlet$GetCredentialAction.class
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/invoker.war/WEB-INF/classes/org/jboss/invocation/http/servlet/InvokerServlet$GetPrincipalAction.class
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/invoker.war/WEB-INF/classes/org/jboss/invocation/http/servlet/NamingFactoryServlet.class
 /usr/local/angel.com/builds/call-server/1/deploy/httpha-invoker.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/deploy.last/farm-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-aop-jdk50.deployer/jrockit-pluggable-instrumentor.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-aop-jdk50.deployer/jboss-aop-jdk50.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-aop-jdk50.deployer/jboss-aspect-library-jdk50.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-aop-jdk50.deployer/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-aop-jdk50.deployer/trove.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-aop-jdk50.deployer/pluggable-instrumentor.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-aop-jdk50.deployer/base-aop.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-bean.deployer/jboss-dependency.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-bean.deployer/jboss-bean-deployer.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-bean.deployer/jboss-container.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-bean.deployer/jboss-microcontainer.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-bean.deployer/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/deploy-hasingleton-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossjca-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/cache-invalidation-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/sqlexception-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/org/jboss/ejb/plugins/keygenerator/uuid/UUIDKeyGeneratorFactory.class
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/org/jboss/ejb/plugins/keygenerator/uuid/UUIDKeyGeneratorFactoryServiceMBean.class
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/org/jboss/ejb/plugins/keygenerator/uuid/UUIDKeyGenerator.class
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/org/jboss/ejb/plugins/keygenerator/uuid/UUIDKeyGeneratorFactoryService.class
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/org/jboss/ejb/plugins/keygenerator/hilo/HiLoKeyGeneratorFactoryMBean.class
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/org/jboss/ejb/plugins/keygenerator/hilo/HiLoKeyGenerator.class
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/org/jboss/ejb/plugins/keygenerator/hilo/HiLoKeyGeneratorFactory.class
 /usr/local/angel.com/builds/call-server/1/deploy/uuid-key-generator.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/conf/web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/ROOT.war/favicon.ico
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/ROOT.war/manager/xform.xsl
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/ROOT.war/index.html
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/ROOT.war/WEB-INF/web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/ROOT.war/css/jboss.css
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/ROOT.war/images/logo.gif
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/server.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/context.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jstl.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jbossweb-service.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jbossweb.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jasper-jdt.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jbossweb-extras.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jsf-libs/jsf-impl.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jsf-libs/jsf-api.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/jsf-libs/jboss-faces.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/META-INF/webserver-xmbean.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web.deployer/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/ejb3-clustered-sfsbcache-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/ejb3-interceptors-aop.xml
 /usr/local/angel.com/builds/call-server/1/deploy/ear-deployer.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jsr88-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/cluster-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/client-deployer-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-ha-local-jdbc.rar
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-local-jdbc.rar
 /usr/local/angel.com/builds/call-server/1/deploy/mail-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/jfreechart.jar
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/console-mgr-classes.jar
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/TopicSubscriptions.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/createStringThresholdMonitorSummary.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/ServerInfo.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPConstructorMetaData.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/manageThresholdMonitor.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/manageStringThresholdMonitor.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/listMonitors.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/manageSnapshot.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/xform.xsl
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/TopicNavigation.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/EntityEjb.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPBinding.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/StatelessEjb.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPMethodMethodCallerChain.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPMetaData.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/createThresholdMonitorSummary.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPIntroductionPointcut.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/Topic.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/listActiveAlarmTable.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPDefaultMetaData.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/index.html
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/applet.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/jboss-web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/tlds/webconsole.tld
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/classes/J2EEFolder.bsh
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/classes/web-console-roles.properties
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/classes/SystemFolder.bsh
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/classes/JNDIView.bsh
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/classes/Classloaders.bsh
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WEB-INF/classes/web-console-users.properties
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/dtree.js
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPConstructorChain.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/SysProperties.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/trash.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/imgfolder.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/join.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/plus.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/line.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/musicfolder.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/cd.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/globe.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/base.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/nolines_minus.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/minusbottom.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/joinbottom.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/folderopen.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/question.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/plusbottom.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/minus.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/folder.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/nolines_plus.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/page.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/img/empty.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/J2EEApp.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/createThresholdMonitor.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/css/dtree.css
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/css/jboss.css
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPMethodConstructorCallerChain.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/EJBModule.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPMethodChain.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/EJB.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/JNDIView.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/MdbEjb.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/createSnapshot.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPConstructorMethodCallerChain.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/WebModule.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/META-INF/MANIFEST.MF
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPFieldMetaData.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/Queue.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPConstructorConstructorCallerChain.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPFieldChain.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/otherimages.jar
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/flash.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/container.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/jndiview.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/server.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/spirale32.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/rubiks.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/bean.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/recycle.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/elements32.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/starfolder.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/service.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/beans.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/spirale.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/serviceset.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/servinghand.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/jboss.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/database.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/smallnet.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/settings32.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/logo.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/card.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/images/EspressoMaker.gif
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/applet.jar
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPMethodMetaData.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/createStringThresholdMonitor.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/AOPClassMetaData.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/Servlet.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/web-console.war/StatefulEjb.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/management/console-mgr.sar/META-INF/MANIFEST.MF
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jbossws-native.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jboss-jaxrpc.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jboss-jaxb-intros.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/wsdl4j.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jboss-jaxws.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/stax-api.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jaxb-api.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jbossws-core.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/wstx.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jbossws-context.war/styles.css
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jbossws-context.war/index.html
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jbossws-context.war/WEB-INF/jboss-web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jbossws-context.war/WEB-INF/web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/xmlsec.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/policy.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jboss-saaj.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/META-INF/MANIFEST.MF
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/META-INF/standard-jaxrpc-client-config.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/META-INF/standard-jaxws-endpoint-config.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/META-INF/standard-jaxrpc-endpoint-config.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/META-INF/standard-jaxws-client-config.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jbossws.beans/META-INF/jboss-beans.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jbossws.sar/jaxb-impl.jar
 /usr/local/angel.com/builds/call-server/1/deploy/jms-ra.rar
 /usr/local/angel.com/builds/call-server/1/deploy/mail-ra.rar
 /usr/local/angel.com/builds/call-server/1/deploy/ejb-deployer.xml
 /usr/local/angel.com/builds/call-server/1/deploy/properties-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web-cluster.sar/jboss-web-cluster.aop
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-web-cluster.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/displayMBeans.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/cluster/clusterView.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/cluster/index.html
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/cluster/bootstrap.html
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/checkJNDI.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/jboss-web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/web.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/html/JMXOpsAccessControlFilter.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/html/ClusteredConsoleServlet.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/html/HtmlAdaptorServlet.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/control/AttrResultInfo.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/control/OpResultInfo.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/control/Server.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/control/AddressPort.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/model/DomainData.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/WEB-INF/classes/org/jboss/jmx/adaptor/model/MBeanData.class
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/inspectMBean.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/style_master.css
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/displayOpResult.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/jboss.css
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/index.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/META-INF/MANIFEST.MF
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/images/logo.gif
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-console.war/genericError.jsp
 /usr/local/angel.com/builds/call-server/1/deploy/hsqldb-ds.xml
 /usr/local/angel.com/builds/call-server/1/deploy/ejb3-entity-cache-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/schedule-manager-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-xa-jdbc.rar
 /usr/local/angel.com/builds/call-server/1/deploy/hajndi-jms-ds.xml
 /usr/local/angel.com/builds/call-server/1/deploy/bsh-deployer.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-messaging.sar/remoting-bisocket-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-messaging.sar/connection-factories-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-messaging.sar/messaging-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-messaging.sar/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-messaging.sar/META-INF/MANIFEST.MF
 /usr/local/angel.com/builds/call-server/1/deploy/jboss-messaging.sar/destinations-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/jmx-invoker-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/ejb3.deployer/jboss-ejb3.jar
 /usr/local/angel.com/builds/call-server/1/deploy/ejb3.deployer/META-INF/jboss-service.xml
 /usr/local/angel.com/builds/call-server/1/deploy/ejb3.deployer/META-INF/persistence.properties
 /usr/local/angel.com/builds/call-server/1/deploy/ejb3.deployer/jboss-annotations-ejb3.jar
%attr(754,root,jbrunner) /etc/init.d/angel-call
%attr(755,root,root) /etc/logrotate.d/angel-logrotate-call
%dir  /usr/local/angel.com/builds/call-server/1/deploy-hasingleton

%post
#Don't know why this is necessary, but I can't figure out how to get these files owned by jbrunner
chown -R jbrunner:jbrunner  %{config_dest_dir}

if [ "$1" = "1" ] ; then  # first install
	/usr/sbin/alternatives --install /usr/local/angel.com/services/call/server angel-call-server %{config_dest_dir} 1
	echo /usr/sbin/alternatives --install /usr/local/angel.com/services/call/server angel-call-server %{config_dest_dir} 1
	
	ln -s -T /usr/local/angel.com/services/call/server /usr/local/angel.com/jboss-versions/jboss-eap-4.3.0.GA_CP04/jboss-as/server/call 
	ln -s -T /var/log/angel/jboss-call %{config_dest_dir}/log 

	echo ln -s -T /usr/local/angel.com/services/call/server /usr/local/angel.com/jboss-versions/jboss-eap-4.3.0.GA_CP04/jboss-as/server/call 
	echo ln -s -T /var/log/angel/jboss-call %{config_dest_dir}/log 
	
	
else
	echo "Already installed"
fi



%preun
if [ "$1" = "0" ] ; then  # last uninstall
	/usr/sbin/alternatives --remove angel-call-server %{config_dest_dir}
	echo /usr/sbin/alternatives --remove angel-call-server %{config_dest_dir}
	rm /usr/local/angel.com/jboss-versions/jboss-eap-4.3.0.GA_CP04/jboss-as/server/call
	echo rm /usr/local/angel.com/jboss-versions/jboss-eap-4.3.0.GA_CP04/jboss-as/server/call
else
	echo "Not the last one"
fi

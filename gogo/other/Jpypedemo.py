import jpype
import time

#jdk版本不兼容
map={}
map['password']="e10adc3949ba59abbe56e057f20f883e"
map['time_stamp']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
map["deviceId"]="866874034234915";
map["channel_id"]="12";
map["game_id"]="1128";
map["phone_mob"]="chen001";

jvmPsth=jpype.getDefaultJVMPath() #得到jvm.dll路径
classpath="D:\\anzhuang\\demp.jar"
jvmArg="-Djava.class.path="+classpath
print(jvmArg)
if not jpype.isJVMStarted():
    jpype.startJVM(jvmPsth,jvmArg)
javaClass=jpype.JClass("testdemo.test.RUA")
print(javaClass)
javaInstance=javaClass()
test=javaInstance.URA(map)
print(test)
#jpype.java.lang.System.out.println( 'hello world! ' )
jpype.shutdownJVM()


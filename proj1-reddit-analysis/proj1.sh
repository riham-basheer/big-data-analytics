# ------------------------------------------------------------- #
# A shell script for the CIE 427 - Mini-Project 1               #
#                  Hadoop EcoSystem                             #
# Last update: November 13, 2021                                #
# ------------------------------------------------------------- #
# Usage Instructions                                            #
# 1. Set JAVA_HOME and HADOOP_HOME below to point to their      #
#    correct paths on your machine.                             #
# 2. Add the following line (including the dot at the beginning #
#    to the end of your ~/.bashrc file,                         #
#    . /absolute/path/to/this/script                            #
# ------------------------------------------------------------- #
# NOTE                                                          #
# The map-reduce job should be located in the <job> directory   #
# ------------------------------------------------------------- #
# ALL THE PATHS USED IN THE SCRIPT MUST NOT INCLUDE ANY SPACES! #
#                                                               #
# This includes JAVA_HOME, HADOOP_HOME, the current working     #
# directory and the <job> directory!                            #
# ------------------------------------------------------------- #



export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME='/mnt/c/Users/cyber/Desktop/BA/BigData/hadoop-3.3.1'
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar:${HADOOP_HOME}/share/hadoop/tools/lib/*



function start-hdfs { 
    hdfs namenode -format;
    $HADOOP_HOME/sbin/start-dfs.sh;
    hdfs dfs -mkdir /user;
    hdfs dfs -mkdir /user/$USER
}

function start-yarn { 
    $HADOOP_HOME/sbin/start-yarn.sh
}

function pass-ssh {
    #sudo service ssh restart;                      # Uncomment if permission-22 denied 
    ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa;
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys;
    chmod 0600 ~/.ssh/authorized_keys
}

function upload-files {
    if [ $# != 1 ]; then
        echo "Usage: upload-files <directory-to-upload>"
        return
    fi 
    
    JOB=$1;
    
    hdfs dfs -mkdir myJob;
    hdfs dfs -put $JOB/* myJob
}

function delete-files { 
    hdfs dfs -rm -r /user/$USER;
    hdfs dfs -mkdir /user/$USER
}

function stop-ALL {
    $HADOOP_HOME/sbin/stop-dfs.sh;
    $HADOOP_HOME/sbin/stop-yarn.sh
}

function mapred { 
    if [ $# != 1 ]; then
        echo "Usage: mapred <job>"
        return
    fi 

    JOB=$1;

    hadoop org.apache.hadoop.streaming.HadoopStreaming \
    -files $JOB/mapper.py,$JOB/reducer.py \
    -input $JOB/input \
    -output $JOB/output \
    -mapper mapper.py \
    -reducer reducer.py;
    hdfs dfs -get $JOB/output myJob/output
}
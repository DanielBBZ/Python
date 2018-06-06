#/bin/bash
export PATH=$PATH:/usr/local/bin

logfile="/workspace/ws03/IData/Users/Daniel/Support/clustertest/movefiles.sh.log"
echo "==============================================================" >> $logfile
## Check machine name to assign environment variables
outputPath="NOT SET"

if [ "$HOSTNAME" = "Test-03" ];
then
   outputPath="/workspace/ws03/IData/Users/Daniel/Test"
else
   echo "Machine is not found in list"
   exit
fi
#####################################################################
mkdir -p "$3/_rsyncLog"
if [ "$2" = "alv" ]; then
	rsyncCommand="$HOSTNAME: rsync ALV files only $outputPath/$1/* to $3/"
	echo "$rsyncCommand" >> $logfile
	rsync -azrih --log-file="$3/_rsyncLog/$2_$HOSTNAME.log" --prune-empty-dirs --include="*/" --include='*.'{alv,log,txt} --exclude="*" $outputPath/$1/* $3/
elif [ "$2" = "bam" ];
then
	rsyncCommand="$HOSTNAME: rsync BAM files only $outputPath/$1/* to $3/"
	echo "$rsyncCommand" >> $logfile
	rsync -azrih --log-file="$3/_rsyncLog/$2_$HOSTNAME.log" --prune-empty-dirs --include="*/" --include='*.'{bam,bas,bim,bai} --exclude="*" $outputPath/$1/* $3/
elif [ "$2" = "all" ];
then
	rsyncCommand="$HOSTNAME: rsync BAM files only $outputPath/$1/* to $3/"
	echo "$rsyncCommand" >> $logfile
	rsync -azrih --log-file="$3/_rsyncLog/$2_$HOSTNAME.log" --prune-empty-dirs --include="*/" --exclude="*.fastq.gz" $outputPath/$1/* $3/
elif [ "$2" = "DELETE" ];
then
	rsyncCommand="$HOSTNAME: DELETE THE FOLDER $outputPath/$1 !!!!!!"
	echo "$rsyncCommand" >> $logfile
	rm -rf $outputPath/$1
else
   echo "Please set file type to move" >> $logfile
   exit
fi







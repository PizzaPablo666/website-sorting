while read line;
do
url="https://"
url+="${line}"
echo "${url}"

header=`curl -s -o /dev/null --max-time 15 -D - ${url} | grep "Location" | tr -d '\r'`
redir_url=$url
while [[ $header == *"Location"* ]];
do	
	
	location=`echo $header | cut -d " " -f2`
	if [[ ($location != *"http"*) && ($location != *"https"*) ]]; then
		length=${#url}
		((length--))
		if [[ "${url:$length:1}" == "/" ]];then
			location=`echo $location | cut -c 2-`
		fi
		url+=$location
		
	else
		url=$location
	fi
	redir_url+=";$url"


	header=`curl -s -o /dev/null --max-time 15 -D - ${url} | grep "Location" | tr -d '\r'`
done

echo $redir_url >> redirect_https.txt


done < modif.txt






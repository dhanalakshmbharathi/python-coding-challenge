#!/bin/bash
FILE="/tmp/data"

if [[ ${UID} -ne 0 ]]
then
 echo "Please run with sudo or as root." >&2
 exit 1
fi

#checks if username is supplied
if [[ ${#} -lt 1 ]]
then
  echo "Usage: ${0} USER_NAME [COMMENT]..." 1>&2
  exit 1
fi


USER_NAME=${1}
shift
COMMENT="${*}"

#Generate password for the user
S1=$(echo '!@#$%^*()_+=')
SPECIAL_CHARACTER=$(echo "${S1}" | fold -w1 | shuf | head -c1)
PASS=$(date +%s%N${RANDOM} | sha256sum | head -c2)
PASSWORD=${PASS}${SPECIAL_CHARACTER}

#user add with comments and username
useradd -c "${COMMENT}" -m ${USER_NAME} &> /dev/null


# Check to see if the useradd command succeeded.
if [[ "${?}" -ne  0 ]]
then 
   echo "The account could not be created" >&2 
   exit 1
else
    echo "The user is added" 1>> ${FILE}
fi


#set password to the account
echo ${PASSWORD} | passwd --stdin ${USER_NAME} &>/dev/null



# Check to see if the passwd command succeeded.
if [[ "${?}" -ne  0 ]]
then 
   echo "The Password could not be set." >&2 
   exit 1
else
   echo "The password is set" 1>> ${FILE}
fi



# Display the username, password, and the host where the user was created.

echo "USER_DETAILS:"
echo " username: ${USER_NAME}"
echo " password: ${PASSWORD}"
echo " host: ${HOSTNAME} "

# Force password change on first login.
passwd -e ${USER_NAME} &> /dev/null


exit 0

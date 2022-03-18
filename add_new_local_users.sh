#!/bin/bash

#checks if its execute only by root users
if [[ ${UID} -ne 0 ]]
then
  echo "Please run with sudo or as root."
  exit 1
fi

#checks if username is supplied
if [[ ${#} -lt 1 ]]
then
  echo "Usage: ${0} USER_NAME [COMMENT]..."
  exit 1
fi

#split arguments

#my_code
# count=0
# while [[ "${#}" -gt 0 && count -lt 2 ]]
# do
#   USER_NAME="${1}"
#   shift
#   COMMENT="${*}"
#   count=2
# done

#simpler one
#USER_NAME
USER_NAME="${1}"

#the rest of parameters are for the account comments
shift
COMMENT="${*}"

#Generate password for the user
S1=$(echo '!@#$%^*()_+=')
SPECIAL_CHARACTER=$(echo "${S1}" | fold -w1 | shuf | head -c1)
PASS=$(date +%s%N${RANDOM} | sha256sum | head -c2)
PASSWORD=${PASS}${SPECIAL_CHARACTER}

#user add with comments and username
useradd -c "${COMMENT}" -m ${USER_NAME} 

# Check to see if the useradd command succeeded.
if [[ "${?}" -ne  0 ]]
then 
   echo "The account could not be created"
   exit 1
else
    echo "The user is added"
fi

#set password to the account
echo ${PASSWORD} | passwd --stdin ${USER_NAME}



# Check to see if the passwd command succeeded.
if [[ "${?}" -ne  0 ]]
then 
   echo "The Password could not be set."
   exit 1
else
   echo "The password is set"
fi



# Display the username, password, and the host where the user was created.
echo
echo "USER_DETAILS:"
echo
echo " username: ${USER_NAME}"
echo " password: ${PASSWORD}"
echo " host: "${HOSTNAME}" "

# Force password change on first login.
passwd -e ${USER_NAME}

exit 0
# Make sure the script is being executed with superuser privileges.
if [[ "${UID}" -ne 0 ]]
then 
  echo "Please run with sudo or as root."
  exit 1
fi
# Get the username (login).
read -p "Enter the username: " USER_NAME

# Get the real name (contents for the description field).
read -p " Enter the full name of the user: " COMMENT

# Get the password.
read -p " Enter the password for first login: " PASSWORD

# Create the user with the password.
useradd -c "${COMMENT}" -m ${USER_NAME} 

# Check to see if the useradd command succeeded.
if [[ "${?}" -ne  0 ]]
then 
   echo "The account could not be created"
   exit 1
else
    echo "The user is added"
fi
# Set the password.
echo ${PASSWORD} | passwd --stdin ${USER_NAME}
# Check to see if the passwd command succeeded.
if [[ "${?}" -ne  0 ]]
then 
   echo "The Password could not be set."
   exit 1
else
   echo "The password is set"
fi
# Force password change on first login.
passwd -e ${USER_NAME}
# Display the username, password, and the host where the user was created.
echo " username: ${USER_NAME}"
echo " password: ${PASSWORD}"
echo " host: "${HOSTNAME}" "

exit 0
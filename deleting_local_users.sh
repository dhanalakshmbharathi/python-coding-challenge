#!/bin/bash
# Display the usage and exit.
ARCHIVE_DIR="/tmp/archive"
usage() {
    echo " USAGE: ${0}  [-dra]  USER USER_NAME" 
    echo "Disable a local linux account" 
    echo "OPTIONS" 
    echo " -d  Deletes accounts instead of disabling them." 
    echo "-r  Removes the home directory associated with the account(s)." 
    echo "-a  Creates an archive of the home directory associated with the accounts(s)."
    exit 1
}


# Make sure the script is being executed with superuser privileges.
if [[ ${UID} -ne 0 ]]
then 
    echo "Please run with sudo or as root." >&2
    exit 1
fi
# Parse the options.
while getopts dra OPTION
do 
  case ${OPTION} in
    d)
     TO_DELETE_ACCOUNT="true"
     ;;
    r)
      TO_REMOVE_HOMEDIR="-r"
      ;;
    a)
      TO_CREATE_ARCHIVE="true"
      ;;
    
    ?)
      usage
      ;;
  esac
done

# Remove the options while leaving the remaining arguments.
shift "$(( OPTIND - 1 ))"


# If the user doesn't supply at least one argument, give them help.
if [[ "${#}" -lt 1 ]]
then
    usage
fi
# Loop through all the usernames supplied as arguments.
for USERNAME in "${@}"
do 
  echo "Processing User : ${USERNAME}"
 # Make sure the UID of the account is at least 1000.
  U=$(id -u ${USERNAME} )
  if [[ ${U} -lt 1000 ]]
  then 
       echo "Refusing to remove the  account with UID ${U}"
       exit 1
  fi
 # Create an archive if requested to do so.
 if [[ "${TO_CREATE_ARCHIVE}" =  "true" ]]
    then  
    # Make sure the ARCHIVE_DIR directory exists.
    if [[ ! -d  "${ARCHIVE}" ]]
    then 
        echo "Creating ${ARCHIVE_DIR} directory."
        mkdir -p ${ARCHIVE_DIR} 
        if [[ ${?} -ne 0 ]]
            then 
                echo "The archive directory ${ARCHIVE_DIR} could not be created." >&2
                exit 1
            fi
        fi

    # Archive the user's home directory and move it into the ARCHIVE_DIR
        HOME_DIR="/home/${USERNAME}"
        ARCHIVE_FILE="${ARCHIVE_DIR}/${USERNAME}.tgz"
        if [[ -d "${HOME_DIR}" ]]
        then
            echo "Archiving ${HOME_DIR} to ${ARCHIVE_FILE}"
            tar -zcf ${ARCHIVE_FILE} ${HOME_DIR} &> /dev/null
            if [[ ${?} -ne 0 ]]
            then 
                echo "Could not create ${ARCHIVE_FILE}" >&2
                exit 1
            fi
        else
            echo "${HOME_DIR} does not exist or is not a directory." >&2
            exit 1
        fi
    fi
     # Delete the user.
    if [[ "${TO_DELETE_ACCOUNT}" = "true" ]]
        then 
            userdel ${TO_REMOVE_HOMEDIR} ${USERNAME}
        
        # Check to see if the userdel command succeeded.  
        # We don't want to tell the user that an account was deleted when it hasn't been.
        if [[ "${?}" -ne 0 ]]
        then 
            echo "The account ${USERNAME} was NOT deleted" >&2
            exit 1
        fi
        echo "The account was deleted"
    else
     chage -E 0 ${USERNAME}
     # Check to see if the chage command succeeded.
     # We don't want to tell the user that an account was disabled when it hasn't been.
     if [[ "${?}" -ne 0 ]]
        then 
            echo "The account ${USERNAME} was NOT disabled" >&2
            exit 1
     fi
     echo "The account was disabled"
    fi
done
exit 0
#!/bin/bash
log() {
    #This function send a message to syslog and to standard output of VERBOSE is true
    local MESSAGE="${@}"
    if [[ "${VERBOSE}" = "true" ]]
    then
      echo "${MESSAGE}"
    fi
    logger -t demo10.sh "${MESSAGE}" #messages are recored in system log /var
}

backup_file(){
  #This function creates a backup of a file.Returns non-Zero status on error.
  local FILE=${1}

  #Makr sure the file exist
  if [[ -f "${FILE}" ]]
  then
      local BACKUP_FILE="/var/tmp/$(basename ${FILE}).$(date +F%-N%)"
      log "Backing up ${FILE} to ${BACKUP_FILE}"
      #The exit status of the function will be the exit status of cp command.
      cp -p ${FILE} ${BACKUP_FILE}
  else
      # The file does not exist , do return a non-zero exit status.
      return 1
  fi

#all  variablles are global in scope, use local keywork to define local variable
# exit status within a function is done using return command. if exit is used within the function / out function it is the exit status for whole script
#so use return statement within function to set the exit status of that function alone


}

readonly VERBOSE="true"
log "hello!"
log "dhanalakshmi bharathi"
backup_file /etc/passwd


# Make a decision based on the exit status of the function.
if [[ "${?}" -eq "0" ]]
then 
    log "File backup succeeded!!"
else
    log "File backup failed!!"
    exit 1
fi


#!/usr/bin/env bash

################################################################################################################
################################################################################################################
# COPY THE 1.0 Grading Website

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
CONF_DIR=${THIS_DIR}/../../../config

if [-z $SUBMITTY_INSTALL_DIR ]; then
	DEBUG_ENABLED=$(jq -r '.debugging_enabled' ${CONF_DIR}/database.json)
else
	DEBUG_ENABLED=$(jq -r '.debugging_enabled' ${SUBMITTY_INSTALL_DIR}/database.json)
fi


bash ${THIS_DIR}/install_submitty/install_site.sh

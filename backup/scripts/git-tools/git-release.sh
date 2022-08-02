#!/bin/bash

VERSION=$1
NOW=`date`

printUsage() {
	echo "Usage: $0 <new version>"
}

DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$DIR/git-common.sh"

PREVIOUS_VERSION=`cat $VERSION_FILE`

if [ -z "$VERSION" ]; then
	printUsage
	updateVersion
	exit
fi

CHANGED_FILES=$(getChangedFiles)
if [ "$CHANGED_FILES" ]; then
	echo "ERROR: You have uncommitted changes - please commit first"
	exit 1
fi

echo "### git co master && git pull origin master && git co develop && git pull origin develop" \
	&& git co master && git pull origin master && git co develop && git pull origin develop \
	&& echo "### git flow release start $VERSION" \
	&& git flow release start $VERSION \
	&& echo $VERSION > $VERSION_FILE \
	&& prependToChangeLog "# Release $VERSION - $NOW\n\n`getCommitMessagesSince $PREVIOUS_VERSION`\n" \
	&& if [ -f "$GIT_TOOLS_HOOKS/git-on-release.sh" ]; then "$GIT_TOOLS_HOOKS/git-on-release.sh" $VERSION; fi \
	&& echo "### git commit $VERSION_FILE $CHANGELOG_FILE" \
	&& git add $VERSION_FILE $CHANGELOG_FILE \
	&& git commit -m "Updated $VERSION_FILE and $CHANGELOG_FILE" \
	&& echo "### git flow release finish -mrelease/$VERSION $VERSION" \
	&& git flow release finish -mrelease/$VERSION $VERSION \
	&& echo "### git push origin master --tags && git push origin develop" \
	&& git push origin master --tags && git push origin develop

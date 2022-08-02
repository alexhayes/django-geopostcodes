#!/bin/bash

# Assume that this script has been imported as a submodule, get top level of parent git repo.
GIT_TOOLS_DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GIT_TOOLS_HOOKS="$GIT_TOOLS_DIR/../git-tools-hooks"
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )/../" && git rev-parse --show-toplevel )"

export CHANGELOG_FILE="$DIR/CHANGELOG.md"
export VERSION_FILE="$DIR/VERSION"
CHANGE_FILE="$DIR/._changed-files.txt"

prependToFile() {
	echo -e "$2" | cat - $1 > .git-hotfix-tmp
	mv .git-hotfix-tmp $1
}
prependToChangeLog() {
	prependToFile "$CHANGELOG_FILE" "$1"
	echo "Please review the CHANGELOG.md before continuing"
	$EDITOR $CHANGELOG_FILE
}
getChangedFiles() {
	(git diff --name-only --diff-filter=ACDMRTUX > $CHANGE_FILE \
		&& git diff --cached --name-only --diff-filter=ACDMRTUX >> $CHANGE_FILE) \
		|| exit $?
	CHANGED_FILES=`cat $CHANGE_FILE`
	rm $CHANGE_FILE
	echo $CHANGED_FILES
}
getCurrentBranch() {
	git branch | sed -n -e 's/^\* \(.*\)/\1/p'
}
updateVersion() {
	echo "### Current VERSION file has version `cat VERSION`"
	echo "### Calling git fetch to get VERSION from origin..."
	git fetch
	echo "### Current version: `git show origin/master:VERSION`"
}
getCommitMessagesSince() {
	git log '--pretty=format:%B' --no-merges $1.. \
		| grep -v "Updated $VERSION_FILE and $CHANGELOG_FILE" \
		| perl -p -e 's/^\n//' \
		| sed -e 's/^\([^-]\)/- \1/g' \
		| sed -e 's/^\(- \)#/\1\\#/g'
}
if [ "$1" = "-h" ]; then
	printUsage
	exit
fi
if [ -f $CHANGE_FILE ]; then
	echo "ERROR: $CHANGE_FILE exists"
	exit 1
fi
if [ ! -f $CHANGELOG_FILE -o ! -f $VERSION_FILE ]; then
	echo "ERROR: $VERSION_FILE and $CHANGELOG_FILE must exist"
	exit 1
fi

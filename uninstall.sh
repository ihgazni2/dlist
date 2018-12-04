#pip3 uninstall main
pip3 uninstall dlist
git rm -r dist
git rm -r build
#git rm -r edict.egg-info
git rm -r dlist.egg-info
rm -r dist
rm -r build
#rm -r elist.egg-info
rm -r dlist.egg-info
git add .
git commit -m "remove old build"

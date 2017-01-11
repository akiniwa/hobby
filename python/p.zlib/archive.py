# coding: utf-8
import os
import zipfile


def makeArchive(fileList, archive, root):
    """
    'fileList' is a list of file names - full path each name
    'archive' is the file name for the archive with a full path
    """
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
    a = zipfile.ZipFile(archive, 'w', compression)

    for f in fileList:
        print "archiving file %s" % (f)
        a.write(f, os.path.relpath(f, root))
    a.close()


def dirEntries(dir_name, subdir, *args):
    # Creates a list of all files in the folder
    '''Return a list of file names found in directory 'dir_name'
    If 'subdir' is True, recursively access subdirectories under 'dir_name'.
    Additional arguments, if any, are file extensions to match filenames. Matched
        file names are added to the list.
    If there are no additional arguments, all files found in the directory are
        added to the list.
    Example usage: fileList = dirEntries(r'H:\TEMP', False, 'txt', 'py')
        Only files with 'txt' and 'py' extensions will be added to the list.
    Example usage: fileList = dirEntries(r'H:\TEMP', True)
        All files and all the files in subdirectories under H:\TEMP will be added
        to the list. '''

    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if not args:
                fileList.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
            # recursively access file names in subdirectories
        elif os.path.isdir(dirfile) and subdir:
            print "Accessing directory:", dirfile
            fileList.extend(dirEntries(dirfile, subdir, *args))
    return fileList


folder = '../p.pil'
makeArchive(dirEntries(folder, True), 'p.pil.zip', folder)

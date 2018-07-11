
import os

def getPath(filename):
    subfixMap = {
        "drawable": [".png", ".jpg"],
        "data": [".dat"]
        }
    folder = None
    for dir in subfixMap:
        subfixs = subfixMap[dir]
        for sub in subfixs:
            if filename.endswith(sub):
                folder = dir
                break
    assert folder, "resParser getPath: unknown file %s" % filename
    filePath = "res/%s/%s" % (folder, filename)
    assert os.path.exists(filePath), "resParser getPath: final path is not exists: %s"\
        % filePath
    # TODO add lang config, such as value-en, value-cn
    return filePath


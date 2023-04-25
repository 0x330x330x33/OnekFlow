import binwalk

def binscan(filename):
    text = "## 数据文件提取\n\n"
    print("binwalk analyse start, target is %s ..." % filename)
    try:
        for module in binwalk.scan(filename, signature=True, quiet=True):
            print ("%s mod:" % module.name)
            text += "| %s Results: | |\n|---|---|\n" % module.name
            for result in module.results:
                print ("\t0x%.8X    %s" % (result.offset, result.description))
                text += "| 0x%.8X | %s |\n" % (result.offset, result.description)
    except binwalk.ModuleException as e:
        print ("Critical failure:", e)
    except Exception as e:
        raise e
    text += "\n"
    return text
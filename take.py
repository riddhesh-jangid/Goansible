def take(module):
    impStr = "import anso."+module+" as "+module
    exec(impStr)
    objStr = module+"."+module+"()"
    obj = eval(objStr)
    return obj


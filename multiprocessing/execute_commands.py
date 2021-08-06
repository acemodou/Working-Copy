import multiprocessing
from exceptions import Exception 

def exec_commands(commands, verbose=False, timeout=None, **kwargs):
    """
    run commands in list of commands
    @param commands: list of commands to run
    @param verbose: (optional) print the command prior to execution; default=False
    @param kwargs: (optional) optional kwargs to route to subprocess target
    @return: list of [{stdout, stderr}, {stdout, stderr}, ...]
    """
    from exceptions import Exception

    class TimeOutException(Exception):
        """ generic timeout exception """
        pass

    commands = [commands] if isinstance(commands, str) else commands

    retvals = list()
    for cmd in commands:
        if verbose: tell(msg=">> {}".format(cmd))

        if isinstance(timeout, (int, float)):
            proc = RunnerProc(func=cmd, kwargs=kwargs)
            proc.start()
            proc.join(timeout)
            if proc.is_alive():
                outp, errp = '', 'timeout exceeded'.format(timeout)
            else:
                outp, errp = cmd, ''
        else:
            subp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
            outp, errp = subp.communicate()

        if errp and re.match(r"timeout exceeded", errp):
            print("target command\n> '{}'".format(cmd))
            raise TimeOutException("command exceeded target timeout={:.3f}-s".format(timeout))

        retvals.append({"stdout": outp, "stderr": errp})

    return retvals if (len(retvals) > 1) else retvals[-1]

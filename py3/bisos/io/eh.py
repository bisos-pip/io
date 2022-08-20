# -*- coding: utf-8 -*-

""" #+begin_org
* *[Summary]* :: A =CS-Lib= for creating and managing BPO's gpg and encryption/decryption.
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['bpoGpg'], }
icmInfo['version'] = '202208073306'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'bpoGpg-Panel.org'
icmInfo['groupingType'] = 'IcmGroupingType-pkged'
icmInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos.crypt/_nodeBase_/fullUsagePanel-en.org][PyFwrk bisos.crypt Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

#import os
import sys
#import select

# import pwd
# import grp
# import collections
# import enum
#

#import traceback

# import collections

# import pathlib

# from bisos.platform import bxPlatformConfig
# from bisos.platform import bxPlatformThis

# from bisos.basics import pattern

# from bisos.bpo import bpo
#from bisos.pals import palsSis
#from bisos.icm import fpath

# from bisos import bpf

# import gnupg

#import logging

#import shutil

# import pykeepass_cache
# import pykeepass

####+BEGIN: bx:icm:py3:func :funcName "read" :funcType "extTyped" :retType "extTyped" :deco "icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /read/ deco=icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)  [[elisp:(org-cycle)][| ]]
#+end_org """
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def read(
####+END:
) -> str:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Reads stdin. Returns a string. -- Uses mutable list.
    #+end_org """

    stdinAsStr = ""
    #if select.select([sys.stdin, ], [], [], 0.0)[0]:
    if not sys.stdin.isatty():

        msgAsList = []
        for line in sys.stdin:
            msgAsList.append(str(line))

        stdinAsStr = str("".join(msgAsList),)

    return stdinAsStr



"""
*  [[elisp:(org-cycle)][| ]]  /EH_/                :: *EH_: ICM Error Handling On Top Of Python Exceptions (EH_ Module)* [[elisp:(org-cycle)][| ]]
"""
"""
**  [[elisp:(org-cycle)][| ]]  Subject      ::== CmndArgs Exceptions (EH_ Module) [[elisp:(org-cycle)][| ]]
"""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_critical_cmndArgsPositional  --   [[elisp:(org-cycle)][| ]]
"""

def EH_critical_cmndArgsPositional(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )
    #raise RuntimeError()
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_critical_cmndArgsOptional    [[elisp:(org-cycle)][| ]]
"""

def EH_critical_cmndArgsOptional(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )
    #raise RuntimeError()
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_critical_usageError    [[elisp:(org-cycle)][| ]]
"""

def EH_critical_usageError(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_usageError: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )
    return(ReturnCode.UsageError)
    #raise RuntimeError()
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_problem_notyet    [[elisp:(org-cycle)][| ]]
"""

def EH_problem_notyet(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_NotYet: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )
    #raise RuntimeError()

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_problem_info    [[elisp:(org-cycle)][| ]]
"""

def EH_problem_info(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_Info: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_problem_usageError -- logger.error (40)  [[elisp:(org-cycle)][| ]]
"""

def EH_problem_usageError(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )

    return (
        eh_problem_usageError(OpOutcome(), *v, **k)
    )

    #raise RuntimeError()


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  eh_problem_usageError -- Captured in Outcome  [[elisp:(org-cycle)][| ]]
"""


def eh_problem_usageError(outcome, *v, **k):
    """
    """
    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    errStr='EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2)
    return(outcome.set(
        opError=OpError.UsageError,
        opErrInfo=errStr,
    ))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_critical_unassigedError    [[elisp:(org-cycle)][| ]]
"""

def EH_critical_unassigedError(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )
    #raise RuntimeError()
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_problem_unassignedError    [[elisp:(org-cycle)][| ]]
"""

def EH_problem_unassignedError(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )
    #raise RuntimeError()

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_critical_oops    [[elisp:(org-cycle)][| ]]
"""

def EH_critical_oops(*v, **k):
    """A Software Error has Occured.
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    print(('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) ))
    logger.critical('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )

    traceback.print_stack()


    #raise RuntimeError()

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_critical_exception    [[elisp:(org-cycle)][| ]]
"""

def EH_critical_exception(e):
    """ Usage Example:
    try: m=2/0
    except Exception as e: icm.EH_critical_exception(e)
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    #fn = FUNC_currentGet()

    outString = format(e)

    logger.critical('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )

    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logger.critical(
        "EH_: {exc_type} {fname} {lineno}"
        .format(
            exc_type=exc_type,
            fname=fname,
            lineno=exc_tb.tb_lineno
        )
    )

    logging.exception(e)

    # Or any of the
    #logger.error("EH_critical_exception", exc_info=True)
    #print(traceback.format_exc())



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_badOutcome    [[elisp:(org-cycle)][| ]]
"""
def EH_badOutcome(outcome):
    print((
        "EH_badOutcome: InvokedBy {invokerName}, Operation Failed: Stdcmnd={stdcmnd} Error={status} -- {errInfo}".
        format(invokerName=outcome.invokerName,
               stdcmnd=outcome.stdcmnd,
               status=outcome.error,
               errInfo=outcome.errInfo,
        )))
    print(('EH_: ' + ' -- ' + ucf.stackFrameInfoGet(2) ))

    return outcome

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || CMND              ::  EH_badLastOutcome    [[elisp:(org-cycle)][| ]]
"""
def EH_badLastOutcome():
    return (
        EH_badOutcome(
            IcmGlobalContext().lastOpOutcome
        ))

def eh_badLastOutcome():
    return (
            IcmGlobalContext().lastOpOutcome
    )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  EH_runTime    [[elisp:(org-cycle)][| ]]
"""

def EH_runTime(*v, **k):
    """
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.error('EH_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )
    raise RuntimeError()



####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:


####+BEGIN: b:prog:file/endOfFile :extraParams nil
""" #+begin_org
* *[[elisp:(org-cycle)][| END-OF-FILE |]]* :: emacs and org variables and control parameters
#+end_org """
### local variables:
### no-byte-compile: t
### end:
####+END:

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

import getpass

#import logging

#import shutil

# import pykeepass_cache
# import pykeepass


import logging
logger = logging.getLogger('root')

handler = logging.StreamHandler()
handler.setLevel(0)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s -\t%(pathname)s[%(lineno)d]:%(funcName)s():\t%(msg)s")
    )
logger.addHandler(handler)

logger.info('connecting')

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
*  [[elisp:(org-cycle)][| ]]  /Outputs Control/    :: *LOG_: ICM Logging Control -- On top of Standard of Python Logging* [[elisp:(org-cycle)][| ]]
"""

#LOGGER = 'Icm.Python.Logger'
LOGGER = 'Icm'
CONSL_LEVEL_RANGE = list(range(0, 51))
#FORMAT_STR = '%(asctime)s %(levelname)s %(message)s'
FORMAT_STR = '%(levelname)s %(message)s -- %(asctime)s'


####+BEGIN: bx:icm:python:func :funcName "logFileName" :funcType "anyOrNone" :retType "str" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /logFileName/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def logFileName():
####+END:
    return (
        "/tmp/{userName}-ICM.log".format(
            userName=getpass.getuser()
        )
    )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  getConsoleLevel    [[elisp:(org-cycle)][| ]]
"""

def getConsoleLevel(args):
    level = args.verbosityLevel
    if level is None: return
    try: level = int(level)
    except: pass
    if level not in CONSL_LEVEL_RANGE:
        args.verbosityLevel = None
        print('warning: console log level ', level, ' not in range 1..50.')
        return
    return level

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class            ::  LOG_Control  -- logging: debug(TM_), info(LOG_), warning(EH_), error(EH_), critical(EH_)   [[elisp:(org-cycle)][| ]]
"""

class LOG_Control():
    """ICM Logging on top of basic Logging.
    """

    args = None
    logger = None
    fh = None
    level = None

    def __init__(self):
        pass

    def loggerSet(self, args):
        """
        """

        #print( args )    #TEMP

        self.__class__.args = args

        logger = logging.getLogger(LOGGER)

        self.__class__.logger = logger

        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT_STR)
        ## Add FileHandler
        fh = logging.FileHandler(logFileName())
        fh.name = 'File Logger'
        fh.level = logging.WARNING
        fh.formatter = formatter
        logger.addHandler(fh)

        self.__class__.fh = fh

        ## Add (optionally) ConsoleHandler
        level = getConsoleLevel(args)

        self.__class__.level = level

        #print( 'level= ' + str(level) )  # TEMP

        if level is not None:
            #print( stackFrameInfoGet(1) )  # TEMP
            ch = logging.StreamHandler()
            ch.name = 'Console Logger'
            ch.level = level
            ch.formatter = formatter
            logger.addHandler(ch)
            #print( stackFrameInfoGet(1) )  # TEMP
        return logger

    def loggerSetLevel(self, level):
        """
        """

        #print( args )    #TEMP

        #self.__class__.args = args

        logger = logging.getLogger(LOGGER)

        self.__class__.logger = logger

        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT_STR)
        ## Add FileHandler
        fh = logging.FileHandler(logFileName())
        fh.name = 'File Logger'
        fh.level = logging.WARNING
        fh.formatter = formatter
        logger.addHandler(fh)

        self.__class__.fh = fh

        ## Add (optionally) ConsoleHandler
        #level = getConsoleLevel(args)

        self.__class__.level = level

        #print( 'level= ' + str(level) )  # TEMP

        if level is not None:
            #print( stackFrameInfoGet(1) )  # TEMP
            ch = logging.StreamHandler()
            ch.name = 'Console Logger'
            ch.level = level
            ch.formatter = formatter
            logger.addHandler(ch)
            #print( stackFrameInfoGet(1) )  # TEMP
        return logger

    def loggerGetLevel(self, ):
        """
        """
        return(self.__class__.level)


    def loggerReset(self):
        logger = self.__class__.logger
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT_STR)
        fh = self.__class__.fh
        fh.formatter = formatter

    def loggerGet(self):
        return self.__class__.logger


"""
*  [[elisp:(org-cycle)][| ]]  /LOG_/               :: *LOG_: Significant Event Which Is Not An Error* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  LOG_note  -- logging.info (20) -- bxf.info.note() -- bxf.info.op.note(outcome,).log()  [[elisp:(org-cycle)][| ]]
"""

def LOG_note(*v, **k):
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

    logger.info( 'LOG_: ' + outString )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  LOG_here  -- logging.info (20) -- bxf.info.here() -- bxf.info.op.here(outcome,)  [[elisp:(org-cycle)][| ]]
"""

def LOG_here(*v, **k):
    """Mark file and line -- do the equivalent of a print statement.
    """
    logControler = LOG_Control()
    logger = logControler.loggerGet()

    fn = ucf.FUNC_currentGet()
    argsLength =  ucf.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.info('LOG_: ' + outString + ' -- ' + ucf.stackFrameInfoGet(2) )




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

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
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['eh'], }
icmInfo['version'] = '202208304656'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'eh-Panel.org'
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

from bisos import bpf
from bisos import io

# import gnupg

import logging

#import shutil

# import pykeepass_cache
# import pykeepass

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "EH: ICM Error Handling On Top Of Python Exceptions" :anchor "" :extraInfo " (EH_ Module)"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _EH: ICM Error Handling On Top Of Python Exceptions_: |]]   (EH_ Module)  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END

####+BEGIN: bx:cs:py3:func :funcName "critical_cmndArgsPositional" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /critical_cmndArgsPositional/  [[elisp:(org-cycle)][| ]]
#+end_org """
def critical_cmndArgsPositional(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )
    #raise RuntimeError()

####+BEGIN: bx:cs:py3:func :funcName "critical_cmndArgsOptional" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /critical_cmndArgsOptional/  [[elisp:(org-cycle)][| ]]
#+end_org """
def critical_cmndArgsOptional(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )
    #raise RuntimeError()

####+BEGIN: bx:cs:py3:func :funcName "critical_usageError" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /critical_usageError/  [[elisp:(org-cycle)][| ]]
#+end_org """
def critical_usageError(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_usageError: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )
    return(ReturnCode.UsageError)
    #raise RuntimeError()

####+BEGIN: bx:cs:py3:func :funcName "problem_notyet" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /problem_notyet/  [[elisp:(org-cycle)][| ]]
#+end_org """
def problem_notyet(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_NotYet: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )
    #raise RuntimeError()

####+BEGIN: bx:cs:py3:func :funcName "problem_info" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /problem_info/  [[elisp:(org-cycle)][| ]]
#+end_org """
def problem_info(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    logger.critical('EH_Info: ' + format(*v, **k) + ' -- ' + bpf.ast.stackFrameInfoGet(2) )

    return

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_Info: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )

####+BEGIN: bx:cs:py3:func :funcName "problem_usageError" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /problem_usageError/  [[elisp:(org-cycle)][| ]]
#+end_org """
def problem_usageError(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )

    return (
        eh_problem_usageError(OpOutcome(), *v, **k)
    )

    #raise RuntimeError()


####+BEGIN: bx:cs:py3:func :funcName "eh_problem_usageError" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /eh_problem_usageError/  [[elisp:(org-cycle)][| ]]
#+end_org """
def eh_problem_usageError(
####+END:
        outcome,
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    errStr='EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2)
    return(outcome.set(
        opError=OpError.UsageError,
        opErrInfo=errStr,
    ))


####+BEGIN: bx:cs:py3:func :funcName "critical_unassigedError" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /critical_unassigedError/  [[elisp:(org-cycle)][| ]]
#+end_org """
def critical_unassigedError(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.critical('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )
    #raise RuntimeError()

####+BEGIN: bx:cs:py3:func :funcName "critical_oops" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /critical_oops/  [[elisp:(org-cycle)][| ]]
#+end_org """
def critical_oops(
####+END:
        *v,
        **k,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    print(('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) ))
    logger.critical('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )

    traceback.print_stack()


    #raise RuntimeError()

####+BEGIN: bx:cs:py3:func :funcName "critical_exception" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /critical_exception/  [[elisp:(org-cycle)][| ]]
#+end_org """
def critical_exception(
####+END:
        e,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Usage Example:
    try: m=2/0
    except Exception as e: icm.EH_critical_exception(e)
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    #fn = FUNC_currentGet()

    outString = format(e)

    logger.critical('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )

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

####+BEGIN: bx:cs:py3:func :funcName "badOutcome" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /badOutcome/  [[elisp:(org-cycle)][| ]]
#+end_org """
def badOutcome(
####+END:
        outcome,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    print((
        "EH_badOutcome: InvokedBy {invokerName}, Operation Failed: Stdcmnd={stdcmnd} Error={status} -- {errInfo}".
        format(invokerName=outcome.invokerName,
               stdcmnd=outcome.stdcmnd,
               status=outcome.error,
               errInfo=outcome.errInfo,
        )))
    print(('EH_: ' + ' -- ' + bpf.ast.stackFrameInfoGet(2) ))

    return outcome

####+BEGIN: bx:cs:py3:func :funcName "badLastOutcome" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /badLastOutcome/  [[elisp:(org-cycle)][| ]]
#+end_org """
def badLastOutcome(
####+END:
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """
    return (
        EH_badOutcome(
            cs.G.lastOpOutcome
        ))

####+BEGIN: bx:cs:py3:func :funcName "eh_badLastOutcome" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /eh_badLastOutcome/  [[elisp:(org-cycle)][| ]]
#+end_org """
def eh_badLastOutcome(
####+END:
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    return (
            cs.G.lastOpOutcome
    )


####+BEGIN: bx:cs:py3:func :funcName "runTime" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /runTime/  [[elisp:(org-cycle)][| ]]
#+end_org """
def runTime(
####+END:
        *v,
        **k,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    logControler = io.log.Control()
    logger = logControler.loggerGet()

    fn = bpf.ast.FUNC_currentGet()
    argsLength =  bpf.ast.FUNC_argsLength(fn, v, k)

    if argsLength == 2:   # empty '()'
        outString = ''
    else:
        outString = format(*v, **k)

    logger.error('EH_: ' + outString + ' -- ' + bpf.ast.stackFrameInfoGet(2) )
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

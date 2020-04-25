# -*- coding: utf_8 -*-
"""Semantic Grep Helpers."""
from argparse import Namespace

from semgrep import semgrep_main


def call_semgrep(paths, scan_rules):
    """Call Semgrep."""
    args = Namespace(
        autofix=False,
        config=scan_rules,
        dangerously_allow_arbitrary_code_execution_from_rules=False,
        dump_ast=False,
        error=False,
        exclude=[],
        exclude_dir=[],
        exclude_tests=False,
        generate_config=False,
        include=[],
        json=True,
        lang=None,
        no_rewrite_rule_ids=False,
        output=None,
        pattern=None,
        precommit=False,
        quiet=True,
        r2c=False,
        strict=False,
        target=paths,
        test=False,
        test_ignore_todo=False,
        validate=False,
        verbose=False,
        version=False)
    return semgrep_main.main(args)

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from pyke import knowledge_engine
import pdir

engine = knowledge_engine.engine('/Users/William/Programming/PyKE/test/kbtest')


engine.activate('rule')
engine.get_kb('knowledge').dump_specific_facts()
res, _ = engine.prove_1_goal('knowledge.master(liaoyinan, $language)')
print(res)

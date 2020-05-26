#!/usr/bin/python3
class LockedClass:
    """reduce the burden on your RAM,
     slots to prevent the dynamic creation of attributes"""
    __slots__ = ['first_name']

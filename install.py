#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Benoit Viguier
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to
# do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from sys import argv
from sys import exit
from shutil import copy2
from shutil import rmtree
import os


def print_help(list_arg):
    print(list_arg[0])
    print("----------------------------------------")
    print("")
    print("basic usage: " + list_arg[0] + " [-f] --install")
    print("")
    print("options:")
    print("-f | force   : remove files when conflict")
    print("-i | install : install the dotfiles")
    print("-r | reset   : restore previous files")
    print("-s | save    : save the current files")
    print("-c | clean   : remove the backup dir")
    exit()


def build_list(excluded, included, dirs, path="."):
    fetch = [x for x in os.listdir(path) if x not in excluded]
    for x in fetch:
        if os.path.isdir(os.path.join(path, x)):
            dirs.append(os.path.join(path, x))
            build_list(excluded, included, dirs, os.path.join(path, x))
        else:
            included.append(os.path.join(path, x))


def init_arrays(path=".", excluded=None):
    if excluded is None:
        excluded = []
    included = []
    dirs = []
    build_list(excluded, included, dirs, path)
    return [x[2:] for x in included], [x[2:] for x in dirs]


def install(save=False, force=False):
    excluded = ['.git', '.idea', '.gitignore', 'install.py', 'backup', 'README.md', 'LICENCE',
                'screenshot']
    included, dirs = init_arrays(".", excluded)
    conflicts = False

    print("build dirs")
    for x in dirs:
        dir_real_path = os.path.expanduser(os.path.join("~", x))
        print("  mkdir -p " + dir_real_path)
        os.makedirs(os.path.join("backup", x), 0o755, True)
        os.makedirs(dir_real_path, 0o755, True)

    print()
    print("link files")
    for x in included:
        print("{}:".format(x))
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), x))
        backup_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.join("backup", x)))
        print("\tfile path: " + file_path)
        symlink_path = os.path.expanduser(os.path.join("~", x))
        print("\tsymlink  : " + symlink_path)

        if os.path.islink(symlink_path) and force:
            print("\tremoving existing symlink")
            os.remove(symlink_path)
        elif os.path.isfile(symlink_path) or os.path.islink(symlink_path):
            print("\tfile exists at path")
            if save or force:
                print("\t-> copy: " + symlink_path + " => " + backup_path)
                copy2(symlink_path, backup_path)
            if force:
                print("\t-> rm  : " + symlink_path)
                os.remove(symlink_path)
                print("\t-> creating symlink")
                os.symlink(file_path, symlink_path)
            else:
                print("\t-> do nothing")
                conflicts = True
            continue

        print("\tcreating symlink")
        os.symlink(file_path, symlink_path)

    if conflicts and not force:
        print()
        print("\tSome files were not linked. Try again with: ./install.py force")


def reset():
    os.makedirs(os.path.join(".", "backup"), 0o755, True)
    if len(os.listdir(os.path.join(".", "backup"))) == 0:
        print("nothing to restore")
        os.rmdir(os.path.join(".", "backup"))
        exit()
    excluded = []
    backups, dirs = init_arrays(os.path.join(".", "backup"), excluded)
    backups = [x[7:] for x in backups]
    dirs = [x[7:] for x in dirs]

    print("build dirs")
    for x in dirs:
        dir_real_path = os.path.expanduser(os.path.join("~", x))
        print("  mkdir -p " + dir_real_path)
        os.makedirs(dir_real_path, 0o755, True)

    print()
    print("copy files back")
    for x in backups:
        print("{}:".format(x))

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.join("backup", x)))
        print("\tfile path : " + file_path)
        symlink_path = os.path.expanduser(os.path.join("~", x))
        print("\tdest path : " + symlink_path)

        if os.path.isfile(symlink_path) or os.path.islink(symlink_path):
            os.remove(symlink_path)

        copy2(file_path, symlink_path)


def parse_args(i, list_arg):
    if i < len(list_arg):
        if list_arg[i] == "force" or list_arg[i] == "-f":
            print("Don't worry, files will be saved in './backup', to remove use 'clean'")
            install(True, True)
            exit()
        if list_arg[i] == "install" or list_arg[i] == "-i":
            install()
            exit()
        elif list_arg[i] == "reset" or list_arg[i] == "-r":
            reset()
            exit()
        elif list_arg[i] == "save" or list_arg[i] == "-s":
            install(True)
            exit()
        elif list_arg[i] == "clean" or list_arg[i] == "-c":
            rmtree("./backup")
            exit()
        elif list_arg[i] == "help" or list_arg[i] == "-h":
            print_help(list_arg)
            exit()
        else:
            print("I don't know what to do")
            exit()
    print_help(list_arg)


parse_args(1, argv)

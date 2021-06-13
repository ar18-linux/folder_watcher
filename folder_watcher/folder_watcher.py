#!/usr/bin/python

import os
import inotify.adapters


def _main():
  inot = inotify.adapters.Inotify()
  inot.add_watch("/tmp")

  for event in inot.event_gen(yield_nones=False):
    (_, type_names, path, filename) = event

    print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
      path, filename, type_names))


if __name__ == "__main__":
  _main()
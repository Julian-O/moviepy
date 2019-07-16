# -*- coding: utf-8 -*-
"""Issue test meant to be run with pytest.

This can't be put with test_issues.py, because it needs
to be the first to run the import."""

try:
    from io import StringIO
except:
    # Python 2.
    from cStringIO import StringIO
import sys

import pytest


def test_issue_985():

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    # Import a package that depends on pygame.

    # Either of these will do. Both is overkill.
    import moviepy.audio.io.preview
    # import moviepy.video.io.preview

    # Not tested: Importing moviepy.video.tools.tracking and calling
    # manual_tracking() which does an import.

    sys.stdout = old_stdout
    assert len(mystdout.getvalue()) == 0, \
        "Unexpected output on import: %s" % mystdout.getvalue()

# Manually tested:
#   Uninstalled PygameSilent.
#   from moviepy.editor import VideoClip, AudioClip
#
#   Call:
#       VideoClip.preview(None)
#   and
#       AudioClip.preview(None)
#
#   Both correctly raised an ImportError with meaningful error messages.


if __name__ == '__main__':
    pytest.main()

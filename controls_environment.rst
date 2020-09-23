Setting up a conda environment for controls
-------------------------------------------

Anaconda has the ability to set up different environments (set ups) for different scenarios. From time to time, it just doesn't like installing things in the base environment (the default that you start with).

In that case, you will need to create and use one for this special case.

In your terminal (windows users: anaconda prompt)

1. ``conda create --name controls`` : This creates a new environment

2. ``conda activate controls`` : This makes is the active environment

3. ``conda install jupyter scipy matplotlib`` : This installs these three packages. It will install a ton of stuff. Good. If you have a missing package warning later, try this command first, restart and see if it solved it.

4. ``conda install -c conda-forge jupyterlab control`` : This looks in a different location to install these two packages. A lot more stuff. Go with "yes".

5. ``pip install vibration_toolbox`` : We may or may not use this, but this is the last (3rd) way to try to install a missing package.

**Each time you open a terminal you will need to type** ``conda activate controls``. You can create shortcuts at the terminal. Mine is ``cac``. If you are using ``bash``, edit your ``.bash_profile`` and add the line ``alias cac="conda activate controls"``. If you use ``zsh``, put the same line in the file ``.zshrc``. To edit those files, use the command ``pico ~/.bash_profile`` or ``pico ~/.zshrc``.

You should now be able to use ``jupyter lab`` and ``jupyter notebook`` from the terminal and view and run the notebooks.

**Don't forget to make sure the controls environment is active before running jupyter!!!**


Mac and Linux
_____________

If you are on a Mac, in terminal, you might try this. First- check which shell you are using. type

.. code-block:: bash

   env | grep SHELL


bash shell
~~~~~~~~~~

If it says ``SHELL=/bin/bash`` or something similar showing ``bash``, then copy and paste this are your prompt::

    cat >> .bash_profile
    alias controls_lab = 'cd ~/Documents/GitHub/Tennessee_Tech_ECE_3210; conda activate controls; git pull jupyter lab'
    alias controls_notebook = 'cd ~/Documents/GitHub/Tennessee_Tech_ECE_3210; conda activate controls; git pull; jupyter notebook'
    alias cac = 'conda activate controls'

Then hit ``CTRL-d``.

Paste::

    source ~/.bash_profile

This will define the commands ``controls_lab`` etc. so you don't have to change directories, etc. It will also automatically update your notes.

zsh shell
~~~~~~~~~~

If it says ``SHELL=/bin/zsh`` or something similar showing ``zsh``, then copy and paste this are your prompt::

    cat >> .zshrc
    alias controls_lab = 'cd ~/Documents/GitHub/Tennessee_Tech_ECE_3210; conda activate controls; git pull jupyter lab'
    alias controls_notebook = 'cd ~/Documents/GitHub/Tennessee_Tech_ECE_3210; conda activate controls; git pull; jupyter notebook'
    alias cac = 'conda activate controls'

Then hit ``CTRL-d``.

Paste::

    source ~/.zshrc

This will define the commands ``controls_lab`` etc. so you don't have to change directories, etc. It will also automatically update your notes.

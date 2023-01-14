# DVC Tutorial

A tutorial on how to use DVC (Data Version Control) in your projects to version large data, models, etc.

## Steps

* To initialize dvc, run:

```bash
dvc init
git commit -m "Initialized dvc"
```

* To track the files (data and models) in the `src` directory, run:

```bash
dvc add src/data src/models
```

* Git prompts you to add the changes made to the repo. Run:

```bash
git add src/data.dvc src/models.dvc
git commit -m "Add files to be tracked by dvc"
```

* To autostage changes (i.e git automatically adds files created by dvc), run:

```bash
core.autostage
```

* To add a remote storage, e.g Google Drive, run:

```bash
dvc add --default <storage_name> gdrive://<your_folder_id>

# e.g
dvc add -d myremote gdrive://0AIac4JZqHhKmUk9PDA

# Push to the remote storage
dvc push  # Assuming there's data to push

git commit -m "Add data"
```

* If for some reason, you deleted your data or model files, run:

```bash
dvc pull
```

* Making changes to a file, run:

```bash
dvc add data/filename

git commit -m "Dataset updates"
dvc push
```

### Switching between versions
  
* The regular workflow is to use git checkout first (to switch a branch or checkout a `.dvc file` version) and then run dvc checkout to sync data:

```bash
git checkout HEAD~1 data/data.xml.dvc
dvc checkout
```

Commit it (no need to do `dvc push` this time since this original version of the dataset was already saved). Run:

```bash
git commit -m "Revert dataset updates"
```

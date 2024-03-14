# thredds-DPC
Creates a THREDDS containerized server that successfully serves the public
CloudSat data, providing both web browser and OPeNDAP URL access to the data.
For experienced THREDDS users, this stands up THREDDS Data Server (TDS) for
serving CloudSat data.

## Running the server/service
On a test machine that has Docker installed:
1. Clone this project
1. Create a directory to contain the THREDDS persistent files and the server's
   log files.
   Examples: /home/cloudsat/thredds-mounts on node1,
   /mnt/data1/fluke/data/thredds-docker on node2.
1. The following directory tree should be created under this directory:
   ```
   ./tomcat
   ./tomcat/logs
   ./thredds
   ./thredds/directory
   ./thredds/logs
   ```
1. Create a directory to contain the sample data. Examples:
   /home/cloudsat/thredds-data on node1, /mnt/data1/fluke/data/CSdata
   on node2.
1. Extract the sample data files from the compressed tar file:
    ```
    cd <to the new test data directory>
    tar -xzvf <your thredds-dpc project dir>/sample-data.tgz
    ```
1. Copy dev.env to .env and fill in the environment variable settings:
   ```
   TDS_MOUNTS_BASE=<directory created in step 2>
   TDS_CS_DATA_DIR=<your test data directory>
   TOMCAT_USER_ID=<The user ID of the project dir owner>
   TOMCAT_GROUP_ID=<The group ID of the project dir owner>
   ```
1. Start the server with `docker-compose up -d thredds-production`

## Connecting to the CloudSat TDS from a browser
### If you have it running on your localhost, use:
`http://localhost:7000/thredds/catalog/catalog.html`
### Or if running the browser from a different host than the server:
`http://<server host>:7000/thredds/catalog/catalog.html`

## Using an OPeNDAP URL to remotely access data within a program
Look at the `opendap_pydap.py` file in this project's `tests` subdirectory.
This program accesses the file remotely through the OPeNDAP URL and transfers
the selected subsets of the data over the network into the program's memory. It
can be run with:
```
docker-compose run --rm test_opendap
```
It defaults to looking for the TDS server on localhost. Change the
`OPENDAP_SERVER` setting in the `docker-compose.yml` file to connect to a
server on a different host. The hard coded file:
`2B-GEOPROF.P1_R05/2008/366/2008366031107_14239_CS_2B-GEOPROF_GRANULE_P1_R05_E02_F00.hdf`
must exist in the data directory, but of course, this can be changed in the
program. It does exists in the sample data.

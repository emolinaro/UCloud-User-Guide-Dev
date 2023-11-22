# Batch Processing

UCloud batch processing apps are scheduled to run as resources permit without end user interaction. The user should select the relevant set of mandatory and/or optional parameters as if the executable program was started in a terminal window. For example, consider the following command line:

```console
$ kallisto quant -i transcripts.idx -b 30 -o results --genomebam -g transcripts.gtf -c chrom.txt reads_1.fastq reads_2.fastq
```

The same command can be executed as an instance of the [Kallisto: quant](kallisto.md) app, available in the UCloud apps catalog. The program options for this particular case can be set by hand from the [front-end page](../guide/submitting.md#setting-parameter-values) or imported via a JSON file, as the one below:

```json

    {
        "siteVersion": 2,
        "request": {
            "application": {
              "name": "kallisto-quant",
              "version": "0.45.0-5"
        },
        "product": {
              "id": "u1-standard-2",
              "category": "u1-standard",
              "provider": "ucloud"
        },
        "name": "Demo",
        "replicas": 1,
        "allowDuplicateJob": false,
        "parameters": {
              "input1": {
                "path": "/home/data/reads_1.fastq",
                "readOnly": false,
                "type": "file"
              },
              "input2": {
                "path": "/home/data/reads_2.fastq",
                "readOnly": false,
                "type": "file"
              },
              "i_var": {
                "path": "/home/data/transcripts.idx",
                "readOnly": false,
                "type": "file"
              },
              "o_var": {
                "value": "results",
                "type": "text"
            },
              "b_var": {
                "value": 30,
                "type": "integer"
              },
              "genomebam_flag": {
                "value": true,
                "type": "boolean"
              },
              "g_var": {
                "path": "/home/data/transcripts.gtf",
                "readOnly": false,
                "type": "file"
              },
              "c_var": {
                "path": "/home/data/chrom.txt",
                "readOnly": false,
                "type": "file"
              }
        },
        "resources": [],
        "timeAllocation": {
              "hours": 1,
              "minutes": 0,
              "seconds": 0
        },
        },
        "machineType": {
            "cpu": 2,
            "memoryInGigs": 12
        }
    }
```

In this example, the input files `reads_1.fastq`, `reads_2.fastq`, `transcripts.idx`, `transcripts.gtf`, and `chrom.txt` are located within the `/home/data` path on UCloud. The directory `results` is created after the run is completed in the [job output folder](../guide/submitting.md#job-completed).

::: {note}

Batch jobs are completed as soon as the executable program is terminated, provided the execution time is lower than the job lifetime and enough resources are available during the runtime.

:::

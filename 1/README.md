# ILAMBv1 experiments

Parameter setup files for experiments
with the NCL version (v1) of ILAMB.

To run an ILAMB experiment on ***beach***
using one of these parameter setup files,
try

```bash
$ qsub -q debug -l pmem=16gb \
> -v parameter_file='/path/to/ILAMB_PARA_SETUP.MsTMIP-le-All' \
> /home/csdms/tools/ILAMB/CODES/run_ilamb.sh -m ae -M <your-email>
```

replacing `<your-email>` with your email address
and `/path/to/ILAMB_PARA_SETUP.MsTMIP-le-All`
with the fully qualified path to the ILAMB parameter setup file.

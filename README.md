This tool is used to build a custom OVA of the C8Kv.

Basic instructions:
- Untar the original OVA into a dedicated directory
- Create an Output directory
- Edit includes.py to reflect the OVA and Output directories
- Copy the OVF file from the OVA directory to the Output directory.  Rename to format.ovf.  Make any desired manual edits.
- Edit parameters.csv to reflect the parameters for all the custom OVAs you want.  Parameters can match any of the parameters in the Virtual Hardware / Product section of the OVF file.  CSV headers must match the parameter names.  Hostname is required and will be used as the OVA name

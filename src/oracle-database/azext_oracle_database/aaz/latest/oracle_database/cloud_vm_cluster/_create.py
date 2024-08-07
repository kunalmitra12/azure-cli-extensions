# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "oracle-database cloud-vm-cluster create",
)
class Create(AAZCommand):
    """Create a CloudVmCluster

    :example: Create VM Cluster
        az oracle-database cloud-vm-cluster create --name <name> --resource-group <resource group> --location <location> --cloud-exadata-infrastructure-id <Exa Infra Id> --cpu-core-count <cpu count> --data-storage-percentage <storage percent> --data-storage-size-in-tbs <storage in TBs> --db-node-storage-size-in-gbs <storage size> --db-servers ['ocid1','ocid2'] --display-name <display name> --gi-version 19.0.0.0 --hostname <host name> --is-local-backup-enabled False --is-sparse-diskgroup-enabled False --license-model <LicenseIncluded/BringYourOwnLicense> --memory-size-in-gbs <memory size> --ssh-public-keys <ssh key> --subnet-id <subnet id> --time-zone <timezeone eg. UTC> --vnet-id <virtual network id>
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/oracle.database/cloudvmclusters/{}", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cloudvmclustername = AAZStrArg(
            options=["-n", "--name", "--cloudvmclustername"],
            help="CloudVmCluster name",
            required=True,
            fmt=AAZStrArgFormat(
                pattern=".*",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.backup_subnet_cidr = AAZStrArg(
            options=["--backup-subnet-cidr"],
            arg_group="Properties",
            help="Client OCI backup subnet CIDR, default is 192.168.252.0/22",
            fmt=AAZStrArgFormat(
                max_length=32,
                min_length=1,
            ),
        )
        _args_schema.cloud_exadata_infrastructure_id = AAZResourceIdArg(
            options=["--exa-infra-id", "--cloud-exadata-infrastructure-id"],
            arg_group="Properties",
            help="Cloud Exadata Infrastructure ID",
        )
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            arg_group="Properties",
            help="The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive. ",
            fmt=AAZStrArgFormat(
                max_length=11,
                min_length=1,
            ),
        )
        _args_schema.cpu_core_count = AAZIntArg(
            options=["--cpu-core-count"],
            arg_group="Properties",
            help="The number of CPU cores enabled on the cloud VM cluster.",
        )
        _args_schema.data_collection_options = AAZObjectArg(
            options=["--collection-options", "--data-collection-options"],
            arg_group="Properties",
            help="Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.",
        )
        _args_schema.data_storage_percentage = AAZIntArg(
            options=["--storage-percent", "--data-storage-percentage"],
            arg_group="Properties",
            help="The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See [Storage Configuration](/Content/Database/Concepts/exaoverview.htm#Exadata) in the Exadata documentation for details on the impact of the configuration settings on storage.",
        )
        _args_schema.data_storage_size_in_tbs = AAZFloatArg(
            options=["--storage-tbs", "--data-storage-size-in-tbs"],
            arg_group="Properties",
            help="The data disk group size to be allocated in TBs.",
        )
        _args_schema.db_node_storage_size_in_gbs = AAZIntArg(
            options=["--node-storage-gbs", "--db-node-storage-size-in-gbs"],
            arg_group="Properties",
            help="The local node storage to be allocated in GBs.",
        )
        _args_schema.db_servers = AAZListArg(
            options=["--db-servers"],
            arg_group="Properties",
            help="The list of DB servers.",
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Display Name",
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )
        _args_schema.domain = AAZStrArg(
            options=["--domain"],
            arg_group="Properties",
            help="The domain name for the cloud VM cluster.",
        )
        _args_schema.gi_version = AAZStrArg(
            options=["--gi-version"],
            arg_group="Properties",
            help="Oracle Grid Infrastructure (GI) software version",
        )
        _args_schema.hostname = AAZStrArg(
            options=["--hostname"],
            arg_group="Properties",
            help="The hostname for the cloud VM cluster.",
            fmt=AAZStrArgFormat(
                max_length=23,
                min_length=1,
            ),
        )
        _args_schema.is_local_backup_enabled = AAZBoolArg(
            options=["--local-backup-enabled", "--is-local-backup-enabled"],
            arg_group="Properties",
            help="If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.",
            default=False,
        )
        _args_schema.is_sparse_diskgroup_enabled = AAZBoolArg(
            options=["--sparse-diskgroup", "--is-sparse-diskgroup-enabled"],
            arg_group="Properties",
            help="If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.",
            default=False,
        )
        _args_schema.license_model = AAZStrArg(
            options=["--license-model"],
            arg_group="Properties",
            help="The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED. ",
            enum={"BringYourOwnLicense": "BringYourOwnLicense", "LicenseIncluded": "LicenseIncluded"},
        )
        _args_schema.memory_size_in_gbs = AAZIntArg(
            options=["--memory-size-in-gbs"],
            arg_group="Properties",
            help="The memory to be allocated in GBs.",
        )
        _args_schema.nsg_cidrs = AAZListArg(
            options=["--nsg-cidrs"],
            arg_group="Properties",
            help="CIDR blocks for additional NSG ingress rules. The VNET CIDRs used to provision the VM Cluster will be added by default.",
        )
        _args_schema.ocpu_count = AAZFloatArg(
            options=["--ocpu-count"],
            arg_group="Properties",
            help="The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.",
        )
        _args_schema.scan_listener_port_tcp = AAZIntArg(
            options=["--scan-listener-port-tcp"],
            arg_group="Properties",
            help="The TCP Single Client Access Name (SCAN) port. The default port is 1521.",
        )
        _args_schema.scan_listener_port_tcp_ssl = AAZIntArg(
            options=["--scan-tcps-port", "--scan-listener-port-tcp-ssl"],
            arg_group="Properties",
            help="The TCPS Single Client Access Name (SCAN) port. The default port is 2484.",
        )
        _args_schema.ssh_public_keys = AAZListArg(
            options=["--ssh-public-keys"],
            arg_group="Properties",
            help="The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.",
        )
        _args_schema.subnet_id = AAZResourceIdArg(
            options=["--subnet-id"],
            arg_group="Properties",
            help="Client subnet",
        )
        _args_schema.system_version = AAZStrArg(
            options=["--system-version"],
            arg_group="Properties",
            help="Operating system version of the image.",
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )
        _args_schema.time_zone = AAZStrArg(
            options=["--time-zone"],
            arg_group="Properties",
            help="The time zone of the cloud VM cluster. For details, see [Exadata Infrastructure Time Zones](/Content/Database/References/timezones.htm).",
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )
        _args_schema.vnet_id = AAZResourceIdArg(
            options=["--vnet-id"],
            arg_group="Properties",
            help="VNET for network connectivity",
        )
        _args_schema.zone_id = AAZStrArg(
            options=["--zone-id"],
            arg_group="Properties",
            help="The OCID of the zone the cloud VM cluster is associated with.",
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )

        data_collection_options = cls._args_schema.data_collection_options
        data_collection_options.is_diagnostics_events_enabled = AAZBoolArg(
            options=["is-diagnostics-events-enabled"],
            help="Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS.",
            default=False,
        )
        data_collection_options.is_health_monitoring_enabled = AAZBoolArg(
            options=["is-health-monitoring-enabled"],
            help="Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS.",
            default=False,
        )
        data_collection_options.is_incident_logs_enabled = AAZBoolArg(
            options=["is-incident-logs-enabled"],
            help="Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS.",
            default=False,
        )

        db_servers = cls._args_schema.db_servers
        db_servers.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )

        nsg_cidrs = cls._args_schema.nsg_cidrs
        nsg_cidrs.Element = AAZObjectArg()

        _element = cls._args_schema.nsg_cidrs.Element
        _element.destination_port_range = AAZObjectArg(
            options=["destination-port-range"],
            help="Destination port range to specify particular destination ports for TCP rules.",
        )
        _element.source = AAZStrArg(
            options=["source"],
            help="Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=128,
                min_length=1,
            ),
        )

        destination_port_range = cls._args_schema.nsg_cidrs.Element.destination_port_range
        destination_port_range.max = AAZIntArg(
            options=["max"],
            help="The maximum port number, which must not be less than the minimum port number. To specify a single port number, set both the min and max to the same value.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=1,
            ),
        )
        destination_port_range.min = AAZIntArg(
            options=["min"],
            help="The minimum port number, which must not be greater than the maximum port number.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=1,
            ),
        )

        ssh_public_keys = cls._args_schema.ssh_public_keys
        ssh_public_keys.Element = AAZStrArg()

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Resource",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.CloudVmClustersCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CloudVmClustersCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/cloudVmClusters/{cloudvmclustername}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "cloudvmclustername", self.ctx.args.cloudvmclustername,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("backupSubnetCidr", AAZStrType, ".backup_subnet_cidr")
                properties.set_prop("cloudExadataInfrastructureId", AAZStrType, ".cloud_exadata_infrastructure_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("clusterName", AAZStrType, ".cluster_name")
                properties.set_prop("cpuCoreCount", AAZIntType, ".cpu_core_count", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("dataCollectionOptions", AAZObjectType, ".data_collection_options")
                properties.set_prop("dataStoragePercentage", AAZIntType, ".data_storage_percentage")
                properties.set_prop("dataStorageSizeInTbs", AAZFloatType, ".data_storage_size_in_tbs")
                properties.set_prop("dbNodeStorageSizeInGbs", AAZIntType, ".db_node_storage_size_in_gbs")
                properties.set_prop("dbServers", AAZListType, ".db_servers")
                properties.set_prop("displayName", AAZStrType, ".display_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("domain", AAZStrType, ".domain")
                properties.set_prop("giVersion", AAZStrType, ".gi_version", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("hostname", AAZStrType, ".hostname", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("isLocalBackupEnabled", AAZBoolType, ".is_local_backup_enabled")
                properties.set_prop("isSparseDiskgroupEnabled", AAZBoolType, ".is_sparse_diskgroup_enabled")
                properties.set_prop("licenseModel", AAZStrType, ".license_model")
                properties.set_prop("memorySizeInGbs", AAZIntType, ".memory_size_in_gbs")
                properties.set_prop("nsgCidrs", AAZListType, ".nsg_cidrs")
                properties.set_prop("ocpuCount", AAZFloatType, ".ocpu_count")
                properties.set_prop("scanListenerPortTcp", AAZIntType, ".scan_listener_port_tcp")
                properties.set_prop("scanListenerPortTcpSsl", AAZIntType, ".scan_listener_port_tcp_ssl")
                properties.set_prop("sshPublicKeys", AAZListType, ".ssh_public_keys", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("subnetId", AAZStrType, ".subnet_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("systemVersion", AAZStrType, ".system_version")
                properties.set_prop("timeZone", AAZStrType, ".time_zone")
                properties.set_prop("vnetId", AAZStrType, ".vnet_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("zoneId", AAZStrType, ".zone_id")

            data_collection_options = _builder.get(".properties.dataCollectionOptions")
            if data_collection_options is not None:
                data_collection_options.set_prop("isDiagnosticsEventsEnabled", AAZBoolType, ".is_diagnostics_events_enabled")
                data_collection_options.set_prop("isHealthMonitoringEnabled", AAZBoolType, ".is_health_monitoring_enabled")
                data_collection_options.set_prop("isIncidentLogsEnabled", AAZBoolType, ".is_incident_logs_enabled")

            db_servers = _builder.get(".properties.dbServers")
            if db_servers is not None:
                db_servers.set_elements(AAZStrType, ".")

            nsg_cidrs = _builder.get(".properties.nsgCidrs")
            if nsg_cidrs is not None:
                nsg_cidrs.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.nsgCidrs[]")
            if _elements is not None:
                _elements.set_prop("destinationPortRange", AAZObjectType, ".destination_port_range")
                _elements.set_prop("source", AAZStrType, ".source", typ_kwargs={"flags": {"required": True}})

            destination_port_range = _builder.get(".properties.nsgCidrs[].destinationPortRange")
            if destination_port_range is not None:
                destination_port_range.set_prop("max", AAZIntType, ".max", typ_kwargs={"flags": {"required": True}})
                destination_port_range.set_prop("min", AAZIntType, ".min", typ_kwargs={"flags": {"required": True}})

            ssh_public_keys = _builder.get(".properties.sshPublicKeys")
            if ssh_public_keys is not None:
                ssh_public_keys.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.backup_subnet_cidr = AAZStrType(
                serialized_name="backupSubnetCidr",
            )
            properties.cloud_exadata_infrastructure_id = AAZStrType(
                serialized_name="cloudExadataInfrastructureId",
                flags={"required": True},
            )
            properties.cluster_name = AAZStrType(
                serialized_name="clusterName",
            )
            properties.compartment_id = AAZStrType(
                serialized_name="compartmentId",
            )
            properties.cpu_core_count = AAZIntType(
                serialized_name="cpuCoreCount",
                flags={"required": True},
            )
            properties.data_collection_options = AAZObjectType(
                serialized_name="dataCollectionOptions",
            )
            properties.data_storage_percentage = AAZIntType(
                serialized_name="dataStoragePercentage",
            )
            properties.data_storage_size_in_tbs = AAZFloatType(
                serialized_name="dataStorageSizeInTbs",
            )
            properties.db_node_storage_size_in_gbs = AAZIntType(
                serialized_name="dbNodeStorageSizeInGbs",
            )
            properties.db_servers = AAZListType(
                serialized_name="dbServers",
            )
            properties.disk_redundancy = AAZStrType(
                serialized_name="diskRedundancy",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.domain = AAZStrType()
            properties.gi_version = AAZStrType(
                serialized_name="giVersion",
                flags={"required": True},
            )
            properties.hostname = AAZStrType(
                flags={"required": True},
            )
            properties.iorm_config_cache = AAZObjectType(
                serialized_name="iormConfigCache",
            )
            properties.is_local_backup_enabled = AAZBoolType(
                serialized_name="isLocalBackupEnabled",
            )
            properties.is_sparse_diskgroup_enabled = AAZBoolType(
                serialized_name="isSparseDiskgroupEnabled",
            )
            properties.last_update_history_entry_id = AAZStrType(
                serialized_name="lastUpdateHistoryEntryId",
            )
            properties.license_model = AAZStrType(
                serialized_name="licenseModel",
            )
            properties.lifecycle_details = AAZStrType(
                serialized_name="lifecycleDetails",
                flags={"read_only": True},
            )
            properties.lifecycle_state = AAZStrType(
                serialized_name="lifecycleState",
            )
            properties.listener_port = AAZIntType(
                serialized_name="listenerPort",
                flags={"read_only": True},
            )
            properties.memory_size_in_gbs = AAZIntType(
                serialized_name="memorySizeInGbs",
            )
            properties.node_count = AAZIntType(
                serialized_name="nodeCount",
                flags={"read_only": True},
            )
            properties.nsg_cidrs = AAZListType(
                serialized_name="nsgCidrs",
            )
            properties.nsg_url = AAZStrType(
                serialized_name="nsgUrl",
                flags={"read_only": True},
            )
            properties.oci_url = AAZStrType(
                serialized_name="ociUrl",
                flags={"read_only": True},
            )
            properties.ocid = AAZStrType()
            properties.ocpu_count = AAZFloatType(
                serialized_name="ocpuCount",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.scan_dns_name = AAZStrType(
                serialized_name="scanDnsName",
                flags={"read_only": True},
            )
            properties.scan_dns_record_id = AAZStrType(
                serialized_name="scanDnsRecordId",
            )
            properties.scan_ip_ids = AAZListType(
                serialized_name="scanIpIds",
                flags={"read_only": True},
            )
            properties.scan_listener_port_tcp = AAZIntType(
                serialized_name="scanListenerPortTcp",
            )
            properties.scan_listener_port_tcp_ssl = AAZIntType(
                serialized_name="scanListenerPortTcpSsl",
            )
            properties.shape = AAZStrType(
                flags={"read_only": True},
            )
            properties.ssh_public_keys = AAZListType(
                serialized_name="sshPublicKeys",
                flags={"required": True},
            )
            properties.storage_size_in_gbs = AAZIntType(
                serialized_name="storageSizeInGbs",
            )
            properties.subnet_id = AAZStrType(
                serialized_name="subnetId",
                flags={"required": True},
            )
            properties.subnet_ocid = AAZStrType(
                serialized_name="subnetOcid",
            )
            properties.system_version = AAZStrType(
                serialized_name="systemVersion",
            )
            properties.time_created = AAZStrType(
                serialized_name="timeCreated",
                flags={"read_only": True},
            )
            properties.time_zone = AAZStrType(
                serialized_name="timeZone",
            )
            properties.vip_ids = AAZListType(
                serialized_name="vipIds",
                flags={"read_only": True},
            )
            properties.vnet_id = AAZStrType(
                serialized_name="vnetId",
                flags={"required": True},
            )
            properties.zone_id = AAZStrType(
                serialized_name="zoneId",
            )

            data_collection_options = cls._schema_on_200_201.properties.data_collection_options
            data_collection_options.is_diagnostics_events_enabled = AAZBoolType(
                serialized_name="isDiagnosticsEventsEnabled",
            )
            data_collection_options.is_health_monitoring_enabled = AAZBoolType(
                serialized_name="isHealthMonitoringEnabled",
            )
            data_collection_options.is_incident_logs_enabled = AAZBoolType(
                serialized_name="isIncidentLogsEnabled",
            )

            db_servers = cls._schema_on_200_201.properties.db_servers
            db_servers.Element = AAZStrType()

            iorm_config_cache = cls._schema_on_200_201.properties.iorm_config_cache
            iorm_config_cache.db_plans = AAZListType(
                serialized_name="dbPlans",
            )
            iorm_config_cache.lifecycle_details = AAZStrType(
                serialized_name="lifecycleDetails",
            )
            iorm_config_cache.lifecycle_state = AAZStrType(
                serialized_name="lifecycleState",
            )
            iorm_config_cache.objective = AAZStrType()

            db_plans = cls._schema_on_200_201.properties.iorm_config_cache.db_plans
            db_plans.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.iorm_config_cache.db_plans.Element
            _element.db_name = AAZStrType(
                serialized_name="dbName",
            )
            _element.flash_cache_limit = AAZStrType(
                serialized_name="flashCacheLimit",
            )
            _element.share = AAZIntType()

            nsg_cidrs = cls._schema_on_200_201.properties.nsg_cidrs
            nsg_cidrs.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.nsg_cidrs.Element
            _element.destination_port_range = AAZObjectType(
                serialized_name="destinationPortRange",
            )
            _element.source = AAZStrType(
                flags={"required": True},
            )

            destination_port_range = cls._schema_on_200_201.properties.nsg_cidrs.Element.destination_port_range
            destination_port_range.max = AAZIntType(
                flags={"required": True},
            )
            destination_port_range.min = AAZIntType(
                flags={"required": True},
            )

            scan_ip_ids = cls._schema_on_200_201.properties.scan_ip_ids
            scan_ip_ids.Element = AAZStrType()

            ssh_public_keys = cls._schema_on_200_201.properties.ssh_public_keys
            ssh_public_keys.Element = AAZStrType()

            vip_ids = cls._schema_on_200_201.properties.vip_ids
            vip_ids.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]

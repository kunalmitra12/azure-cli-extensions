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
    "hdinsight-on-aks cluster library manage",
    is_preview=True,
)
class Manage(AAZCommand):
    """Library management operations on HDInsight on AKS cluster.

    :example: Install maven library 'azure-resourcemanager-hdinsight-containers' to the cluster.
        az hdinsight-on-aks cluster library manage --cluster-name {clustername} -g {resourcesGroup} --cluster-pool-name {clusterpoolname} --action install --libraries '[{maven:{group-id:com.azure.resourcemanager,name:azure-resourcemanager-hdinsight-containers,version:1.0.0-beta.2}}]'

    :example: Uninstall library 'azure-resourcemanager-hdinsight-containers' from the cluster.
        az hdinsight-on-aks cluster library manage --cluster-name {clustername} -g {resourcesGroup} --cluster-pool-name {clusterpoolname} --action uninstall --libraries '[{maven:{group-id:com.azure.resourcemanager,name:azure-resourcemanager-hdinsight-containers,version:1.0.0-beta.2}}]'

    :example: Install pypi library 'Pandas' to the cluster.
        az hdinsight-on-aks cluster library manage --cluster-name {clustername} -g {resourcesGroup} --cluster-pool-name {clusterpoolname} --action install --libraries '[{pypi:{name:pandas}}]'
    """

    _aaz_info = {
        "version": "2024-05-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.hdinsight/clusterpools/{}/clusters/{}/managelibraries", "2024-05-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="The name of the HDInsight cluster.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.cluster_pool_name = AAZStrArg(
            options=["--cluster-pool-name"],
            help="The name of the cluster pool.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.action = AAZStrArg(
            options=["--action"],
            arg_group="Properties",
            help="The library management action.",
            required=True,
            enum={"Install": "Install", "Uninstall": "Uninstall"},
        )
        _args_schema.libraries = AAZListArg(
            options=["--libraries"],
            arg_group="Properties",
            help="The libraries to be installed/updated/uninstalled.",
            required=True,
        )

        libraries = cls._args_schema.libraries
        libraries.Element = AAZObjectArg()

        _element = cls._args_schema.libraries.Element
        _element.maven = AAZObjectArg(
            options=["maven"],
        )
        _element.pypi = AAZObjectArg(
            options=["pypi"],
        )
        _element.remarks = AAZStrArg(
            options=["remarks"],
            help="Remark of the latest library management operation.",
        )

        maven = cls._args_schema.libraries.Element.maven
        maven.group_id = AAZStrArg(
            options=["group-id"],
            help="GroupId of the Maven package.",
            required=True,
        )
        maven.name = AAZStrArg(
            options=["name"],
            help="ArtifactId of the Maven package.",
            required=True,
        )
        maven.version = AAZStrArg(
            options=["version"],
            help="Version of the Maven package.",
        )

        pypi = cls._args_schema.libraries.Element.pypi
        pypi.name = AAZStrArg(
            options=["name"],
            help="Name of the PyPi package.",
            required=True,
        )
        pypi.version = AAZStrArg(
            options=["version"],
            help="Version of the PyPi package.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ClusterLibrariesManageLibraries(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class ClusterLibrariesManageLibraries(AAZHttpOperation):
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
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusterpools/{clusterPoolName}/clusters/{clusterName}/manageLibraries",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "clusterPoolName", self.ctx.args.cluster_pool_name,
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
                    "api-version", "2024-05-01-preview",
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
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("action", AAZStrType, ".action", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("libraries", AAZListType, ".libraries", typ_kwargs={"flags": {"required": True}})

            libraries = _builder.get(".properties.libraries")
            if libraries is not None:
                libraries.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.libraries[]")
            if _elements is not None:
                _elements.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties.libraries[].properties")
            if properties is not None:
                properties.set_prop("remarks", AAZStrType, ".remarks")
                properties.set_const("type", "maven", AAZStrType, ".maven", typ_kwargs={"flags": {"required": True}})
                properties.set_const("type", "pypi", AAZStrType, ".pypi", typ_kwargs={"flags": {"required": True}})
                properties.discriminate_by("type", "maven")
                properties.discriminate_by("type", "pypi")

            disc_maven = _builder.get(".properties.libraries[].properties{type:maven}")
            if disc_maven is not None:
                disc_maven.set_prop("groupId", AAZStrType, ".maven.group_id", typ_kwargs={"flags": {"required": True}})
                disc_maven.set_prop("name", AAZStrType, ".maven.name", typ_kwargs={"flags": {"required": True}})
                disc_maven.set_prop("version", AAZStrType, ".maven.version")

            disc_pypi = _builder.get(".properties.libraries[].properties{type:pypi}")
            if disc_pypi is not None:
                disc_pypi.set_prop("name", AAZStrType, ".pypi.name", typ_kwargs={"flags": {"required": True}})
                disc_pypi.set_prop("version", AAZStrType, ".pypi.version")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            pass


class _ManageHelper:
    """Helper class for Manage"""


__all__ = ["Manage"]

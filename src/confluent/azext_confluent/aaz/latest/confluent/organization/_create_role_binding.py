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
    "confluent organization create-role-binding",
)
class CreateRoleBinding(AAZCommand):
    """Organization role bindings
    """

    _aaz_info = {
        "version": "2024-02-13",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.confluent/organizations/{}/access/default/createrolebinding", "2024-02-13"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.organization_name = AAZStrArg(
            options=["--organization-name"],
            help="Organization resource name",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            options=["--resource-group"],
            help="Resource group name",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.crn_pattern = AAZStrArg(
            options=["--crn-pattern"],
            arg_group="Body",
            help="A CRN that specifies the scope and resource patterns necessary for the role to bind",
        )
        _args_schema.principal = AAZStrArg(
            options=["--principal"],
            arg_group="Body",
            help="The principal User or Group to bind the role to",
        )
        _args_schema.role_name = AAZStrArg(
            options=["--role-name"],
            arg_group="Body",
            help="The name of the role to bind to the principal",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AccessCreateRoleBinding(ctx=self.ctx)()
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

    class AccessCreateRoleBinding(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Confluent/organizations/{organizationName}/access/default/createRoleBinding",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "organizationName", self.ctx.args.organization_name,
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
                    "api-version", "2024-02-13",
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
            _builder.set_prop("crn_pattern", AAZStrType, ".crn_pattern")
            _builder.set_prop("principal", AAZStrType, ".principal")
            _builder.set_prop("role_name", AAZStrType, ".role_name")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.crn_pattern = AAZStrType()
            _schema_on_200.id = AAZStrType()
            _schema_on_200.kind = AAZStrType()
            _schema_on_200.metadata = AAZObjectType()
            _schema_on_200.principal = AAZStrType()
            _schema_on_200.role_name = AAZStrType()

            metadata = cls._schema_on_200.metadata
            metadata.created_at = AAZStrType()
            metadata.deleted_at = AAZStrType()
            metadata.resource_name = AAZStrType()
            metadata.self = AAZStrType()
            metadata.updated_at = AAZStrType()

            return cls._schema_on_200


class _CreateRoleBindingHelper:
    """Helper class for CreateRoleBinding"""


__all__ = ["CreateRoleBinding"]
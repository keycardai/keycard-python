# Zones

Types:

```python
from keycardai_api.types import (
    EncryptionKeyAwsKmsConfig,
    PageInfoPagination,
    Zone,
    ZoneListResponse,
    ZoneListSessionResourceAccessResponse,
)
```

Methods:

- <code title="post /zones">client.zones.<a href="./src/keycardai_api/resources/zones/zones.py">create</a>(\*\*<a href="src/keycardai_api/types/zone_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zone.py">Zone</a></code>
- <code title="get /zones/{zoneId}">client.zones.<a href="./src/keycardai_api/resources/zones/zones.py">retrieve</a>(zone_id, \*\*<a href="src/keycardai_api/types/zone_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/zone.py">Zone</a></code>
- <code title="patch /zones/{zoneId}">client.zones.<a href="./src/keycardai_api/resources/zones/zones.py">update</a>(zone_id, \*\*<a href="src/keycardai_api/types/zone_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zone.py">Zone</a></code>
- <code title="get /zones">client.zones.<a href="./src/keycardai_api/resources/zones/zones.py">list</a>(\*\*<a href="src/keycardai_api/types/zone_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zone_list_response.py">ZoneListResponse</a></code>
- <code title="delete /zones/{zoneId}">client.zones.<a href="./src/keycardai_api/resources/zones/zones.py">delete</a>(zone_id) -> None</code>
- <code title="get /zones/{zoneId}/session-resource-access">client.zones.<a href="./src/keycardai_api/resources/zones/zones.py">list_session_resource_access</a>(zone_id, \*\*<a href="src/keycardai_api/types/zone_list_session_resource_access_params.py">params</a>) -> <a href="./src/keycardai_api/types/zone_list_session_resource_access_response.py">ZoneListSessionResourceAccessResponse</a></code>

## Applications

Types:

```python
from keycardai_api.types.zones import (
    Application,
    ApplicationTrait,
    Metadata,
    MetadataUpdate,
    ApplicationListResponse,
    ApplicationListCredentialsResponse,
    ApplicationListResourcesResponse,
)
```

Methods:

- <code title="post /zones/{zoneId}/applications">client.zones.applications.<a href="./src/keycardai_api/resources/zones/applications/applications.py">create</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/application_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/application.py">Application</a></code>
- <code title="get /zones/{zoneId}/applications/{id}">client.zones.applications.<a href="./src/keycardai_api/resources/zones/applications/applications.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/application.py">Application</a></code>
- <code title="patch /zones/{zoneId}/applications/{id}">client.zones.applications.<a href="./src/keycardai_api/resources/zones/applications/applications.py">update</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/application_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/application.py">Application</a></code>
- <code title="get /zones/{zoneId}/applications">client.zones.applications.<a href="./src/keycardai_api/resources/zones/applications/applications.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/application_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/application_list_response.py">ApplicationListResponse</a></code>
- <code title="delete /zones/{zoneId}/applications/{id}">client.zones.applications.<a href="./src/keycardai_api/resources/zones/applications/applications.py">delete</a>(id, \*, zone_id) -> None</code>
- <code title="get /zones/{zoneId}/applications/{id}/application-credentials">client.zones.applications.<a href="./src/keycardai_api/resources/zones/applications/applications.py">list_credentials</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/application_list_credentials_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/application_list_credentials_response.py">ApplicationListCredentialsResponse</a></code>
- <code title="get /zones/{zoneId}/applications/{id}/resources">client.zones.applications.<a href="./src/keycardai_api/resources/zones/applications/applications.py">list_resources</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/application_list_resources_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/application_list_resources_response.py">ApplicationListResourcesResponse</a></code>

### Dependencies

Types:

```python
from keycardai_api.types.zones.applications import Resource, DependencyListResponse
```

Methods:

- <code title="get /zones/{zoneId}/applications/{id}/dependencies/{dependencyId}">client.zones.applications.dependencies.<a href="./src/keycardai_api/resources/zones/applications/dependencies.py">retrieve</a>(dependency_id, \*, zone_id, id) -> <a href="./src/keycardai_api/types/zones/applications/resource.py">Resource</a></code>
- <code title="get /zones/{zoneId}/applications/{id}/dependencies">client.zones.applications.dependencies.<a href="./src/keycardai_api/resources/zones/applications/dependencies.py">list</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/applications/dependency_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/applications/dependency_list_response.py">DependencyListResponse</a></code>
- <code title="put /zones/{zoneId}/applications/{id}/dependencies/{dependencyId}">client.zones.applications.dependencies.<a href="./src/keycardai_api/resources/zones/applications/dependencies.py">add</a>(dependency_id, \*, zone_id, id, \*\*<a href="src/keycardai_api/types/zones/applications/dependency_add_params.py">params</a>) -> None</code>
- <code title="delete /zones/{zoneId}/applications/{id}/dependencies/{dependencyId}">client.zones.applications.dependencies.<a href="./src/keycardai_api/resources/zones/applications/dependencies.py">remove</a>(dependency_id, \*, zone_id, id) -> None</code>

## ApplicationCredentials

Types:

```python
from keycardai_api.types.zones import (
    BaseFields,
    Credential,
    Password,
    Public,
    PublicKey,
    Token,
    URL,
    ApplicationCredentialCreateResponse,
    ApplicationCredentialListResponse,
)
```

Methods:

- <code title="post /zones/{zoneId}/application-credentials">client.zones.application_credentials.<a href="./src/keycardai_api/resources/zones/application_credentials.py">create</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/application_credential_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/application_credential_create_response.py">ApplicationCredentialCreateResponse</a></code>
- <code title="get /zones/{zoneId}/application-credentials/{id}">client.zones.application_credentials.<a href="./src/keycardai_api/resources/zones/application_credentials.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/credential.py">Credential</a></code>
- <code title="patch /zones/{zoneId}/application-credentials/{id}">client.zones.application_credentials.<a href="./src/keycardai_api/resources/zones/application_credentials.py">update</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/application_credential_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/credential.py">Credential</a></code>
- <code title="get /zones/{zoneId}/application-credentials">client.zones.application_credentials.<a href="./src/keycardai_api/resources/zones/application_credentials.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/application_credential_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/application_credential_list_response.py">ApplicationCredentialListResponse</a></code>
- <code title="delete /zones/{zoneId}/application-credentials/{id}">client.zones.application_credentials.<a href="./src/keycardai_api/resources/zones/application_credentials.py">delete</a>(id, \*, zone_id) -> None</code>

## DelegatedGrants

Types:

```python
from keycardai_api.types.zones import Grant, DelegatedGrantListResponse
```

Methods:

- <code title="get /zones/{zoneId}/delegated-grants/{id}">client.zones.delegated_grants.<a href="./src/keycardai_api/resources/zones/delegated_grants.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/grant.py">Grant</a></code>
- <code title="patch /zones/{zoneId}/delegated-grants/{id}">client.zones.delegated_grants.<a href="./src/keycardai_api/resources/zones/delegated_grants.py">update</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/delegated_grant_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/grant.py">Grant</a></code>
- <code title="get /zones/{zoneId}/delegated-grants">client.zones.delegated_grants.<a href="./src/keycardai_api/resources/zones/delegated_grants.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/delegated_grant_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/delegated_grant_list_response.py">DelegatedGrantListResponse</a></code>
- <code title="delete /zones/{zoneId}/delegated-grants/{id}">client.zones.delegated_grants.<a href="./src/keycardai_api/resources/zones/delegated_grants.py">delete</a>(id, \*, zone_id) -> None</code>

## Providers

Types:

```python
from keycardai_api.types.zones import Provider, ProviderListResponse
```

Methods:

- <code title="post /zones/{zoneId}/providers">client.zones.providers.<a href="./src/keycardai_api/resources/zones/providers.py">create</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/provider_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/provider.py">Provider</a></code>
- <code title="get /zones/{zoneId}/providers/{id}">client.zones.providers.<a href="./src/keycardai_api/resources/zones/providers.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/provider.py">Provider</a></code>
- <code title="patch /zones/{zoneId}/providers/{id}">client.zones.providers.<a href="./src/keycardai_api/resources/zones/providers.py">update</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/provider_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/provider.py">Provider</a></code>
- <code title="get /zones/{zoneId}/providers">client.zones.providers.<a href="./src/keycardai_api/resources/zones/providers.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/provider_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/provider_list_response.py">ProviderListResponse</a></code>
- <code title="delete /zones/{zoneId}/providers/{id}">client.zones.providers.<a href="./src/keycardai_api/resources/zones/providers.py">delete</a>(id, \*, zone_id) -> None</code>

## Resources

Types:

```python
from keycardai_api.types.zones import ResourceListResponse
```

Methods:

- <code title="post /zones/{zoneId}/resources">client.zones.resources.<a href="./src/keycardai_api/resources/zones/resources.py">create</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/resource_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/applications/resource.py">Resource</a></code>
- <code title="get /zones/{zoneId}/resources/{id}">client.zones.resources.<a href="./src/keycardai_api/resources/zones/resources.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/applications/resource.py">Resource</a></code>
- <code title="patch /zones/{zoneId}/resources/{id}">client.zones.resources.<a href="./src/keycardai_api/resources/zones/resources.py">update</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/resource_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/applications/resource.py">Resource</a></code>
- <code title="get /zones/{zoneId}/resources">client.zones.resources.<a href="./src/keycardai_api/resources/zones/resources.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/resource_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/resource_list_response.py">ResourceListResponse</a></code>
- <code title="delete /zones/{zoneId}/resources/{id}">client.zones.resources.<a href="./src/keycardai_api/resources/zones/resources.py">delete</a>(id, \*, zone_id) -> None</code>

## Sessions

Types:

```python
from keycardai_api.types.zones import Session, SessionListResponse
```

Methods:

- <code title="get /zones/{zoneId}/sessions/{id}">client.zones.sessions.<a href="./src/keycardai_api/resources/zones/sessions.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/session.py">Session</a></code>
- <code title="patch /zones/{zoneId}/sessions/{id}">client.zones.sessions.<a href="./src/keycardai_api/resources/zones/sessions.py">update</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/session_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/session.py">Session</a></code>
- <code title="get /zones/{zoneId}/sessions">client.zones.sessions.<a href="./src/keycardai_api/resources/zones/sessions.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/session_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /zones/{zoneId}/sessions/{id}">client.zones.sessions.<a href="./src/keycardai_api/resources/zones/sessions.py">delete</a>(id, \*, zone_id) -> None</code>

## UserAgents

Types:

```python
from keycardai_api.types.zones import UserAgent, UserAgentListResponse
```

Methods:

- <code title="get /zones/{zoneId}/user-agents/{id}">client.zones.user_agents.<a href="./src/keycardai_api/resources/zones/user_agents.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/user_agent.py">UserAgent</a></code>
- <code title="get /zones/{zoneId}/user-agents">client.zones.user_agents.<a href="./src/keycardai_api/resources/zones/user_agents.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/user_agent_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/user_agent_list_response.py">UserAgentListResponse</a></code>

## Users

Types:

```python
from keycardai_api.types.zones import User, UserListResponse
```

Methods:

- <code title="get /zones/{zoneId}/users/{id}">client.zones.users.<a href="./src/keycardai_api/resources/zones/users.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/user.py">User</a></code>
- <code title="get /zones/{zoneId}/users">client.zones.users.<a href="./src/keycardai_api/resources/zones/users.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/user_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/user_list_response.py">UserListResponse</a></code>

## Members

Types:

```python
from keycardai_api.types.zones import ZoneMember, ZoneRole, MemberListResponse
```

Methods:

- <code title="get /zones/{zoneId}/members/{organizationUserId}">client.zones.members.<a href="./src/keycardai_api/resources/zones/members.py">retrieve</a>(organization_user_id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/zone_member.py">ZoneMember</a></code>
- <code title="patch /zones/{zoneId}/members/{organizationUserId}">client.zones.members.<a href="./src/keycardai_api/resources/zones/members.py">update</a>(organization_user_id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/member_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/zone_member.py">ZoneMember</a></code>
- <code title="get /zones/{zoneId}/members">client.zones.members.<a href="./src/keycardai_api/resources/zones/members.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/member_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/member_list_response.py">MemberListResponse</a></code>
- <code title="delete /zones/{zoneId}/members/{organizationUserId}">client.zones.members.<a href="./src/keycardai_api/resources/zones/members.py">delete</a>(organization_user_id, \*, zone_id) -> None</code>
- <code title="post /zones/{zoneId}/members">client.zones.members.<a href="./src/keycardai_api/resources/zones/members.py">add</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/member_add_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/zone_member.py">ZoneMember</a></code>

## Secrets

Types:

```python
from keycardai_api.types.zones import (
    Secret,
    SecretPasswordFields,
    SecretTokenFields,
    SecretRetrieveResponse,
    SecretListResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secrets">client.zones.secrets.<a href="./src/keycardai_api/resources/zones/secrets.py">create</a>(path_zone_id, \*\*<a href="src/keycardai_api/types/zones/secret_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/secret.py">Secret</a></code>
- <code title="get /zones/{zone_id}/secrets/{id}">client.zones.secrets.<a href="./src/keycardai_api/resources/zones/secrets.py">retrieve</a>(id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/secret_retrieve_response.py">SecretRetrieveResponse</a></code>
- <code title="patch /zones/{zone_id}/secrets/{id}">client.zones.secrets.<a href="./src/keycardai_api/resources/zones/secrets.py">update</a>(id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/secret_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/secret.py">Secret</a></code>
- <code title="get /zones/{zone_id}/secrets">client.zones.secrets.<a href="./src/keycardai_api/resources/zones/secrets.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/secret_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /zones/{zone_id}/secrets/{id}">client.zones.secrets.<a href="./src/keycardai_api/resources/zones/secrets.py">delete</a>(id, \*, zone_id) -> None</code>

## PolicySchemas

Types:

```python
from keycardai_api.types.zones import (
    SchemaVersion,
    SchemaVersionWithZoneInfo,
    PolicySchemaListResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/policy-schemas/{version}">client.zones.policy_schemas.<a href="./src/keycardai_api/resources/zones/policy_schemas.py">retrieve</a>(version, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_schema_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/schema_version_with_zone_info.py">SchemaVersionWithZoneInfo</a></code>
- <code title="get /zones/{zone_id}/policy-schemas">client.zones.policy_schemas.<a href="./src/keycardai_api/resources/zones/policy_schemas.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_schema_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_schema_list_response.py">PolicySchemaListResponse</a></code>
- <code title="patch /zones/{zone_id}/policy-schemas/{version}">client.zones.policy_schemas.<a href="./src/keycardai_api/resources/zones/policy_schemas.py">set_default</a>(version, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_schema_set_default_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/schema_version_with_zone_info.py">SchemaVersionWithZoneInfo</a></code>

## Policies

Types:

```python
from keycardai_api.types.zones import Policy, PolicyDraft, PolicyListResponse
```

Methods:

- <code title="post /zones/{zone_id}/policies">client.zones.policies.<a href="./src/keycardai_api/resources/zones/policies/policies.py">create</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy.py">Policy</a></code>
- <code title="get /zones/{zone_id}/policies/{policy_id}">client.zones.policies.<a href="./src/keycardai_api/resources/zones/policies/policies.py">retrieve</a>(policy_id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/policy.py">Policy</a></code>
- <code title="patch /zones/{zone_id}/policies/{policy_id}">client.zones.policies.<a href="./src/keycardai_api/resources/zones/policies/policies.py">update</a>(policy_id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy.py">Policy</a></code>
- <code title="get /zones/{zone_id}/policies">client.zones.policies.<a href="./src/keycardai_api/resources/zones/policies/policies.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_list_response.py">PolicyListResponse</a></code>
- <code title="delete /zones/{zone_id}/policies/{policy_id}">client.zones.policies.<a href="./src/keycardai_api/resources/zones/policies/policies.py">archive</a>(policy_id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/policy.py">Policy</a></code>

### Versions

Types:

```python
from keycardai_api.types.zones.policies import PolicyVersion, VersionListResponse
```

Methods:

- <code title="post /zones/{zone_id}/policies/{policy_id}/versions">client.zones.policies.versions.<a href="./src/keycardai_api/resources/zones/policies/versions.py">create</a>(policy_id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policies/version_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policies/policy_version.py">PolicyVersion</a></code>
- <code title="get /zones/{zone_id}/policies/{policy_id}/versions/{version_id}">client.zones.policies.versions.<a href="./src/keycardai_api/resources/zones/policies/versions.py">retrieve</a>(version_id, \*, zone_id, policy_id, \*\*<a href="src/keycardai_api/types/zones/policies/version_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policies/policy_version.py">PolicyVersion</a></code>
- <code title="get /zones/{zone_id}/policies/{policy_id}/versions">client.zones.policies.versions.<a href="./src/keycardai_api/resources/zones/policies/versions.py">list</a>(policy_id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policies/version_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policies/version_list_response.py">VersionListResponse</a></code>
- <code title="delete /zones/{zone_id}/policies/{policy_id}/versions/{version_id}">client.zones.policies.versions.<a href="./src/keycardai_api/resources/zones/policies/versions.py">archive</a>(version_id, \*, zone_id, policy_id) -> <a href="./src/keycardai_api/types/zones/policies/policy_version.py">PolicyVersion</a></code>

## PolicySets

Types:

```python
from keycardai_api.types.zones import (
    Attestation,
    AttestationStatement,
    PolicySet,
    PolicySetDraft,
    PolicySetManifest,
    PolicySetManifestEntry,
    PolicySetWithBinding,
    PolicySetListResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/policy-sets">client.zones.policy_sets.<a href="./src/keycardai_api/resources/zones/policy_sets/policy_sets.py">create</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_set_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_set_with_binding.py">PolicySetWithBinding</a></code>
- <code title="get /zones/{zone_id}/policy-sets/{policy_set_id}">client.zones.policy_sets.<a href="./src/keycardai_api/resources/zones/policy_sets/policy_sets.py">retrieve</a>(policy_set_id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/policy_set_with_binding.py">PolicySetWithBinding</a></code>
- <code title="patch /zones/{zone_id}/policy-sets/{policy_set_id}">client.zones.policy_sets.<a href="./src/keycardai_api/resources/zones/policy_sets/policy_sets.py">update</a>(policy_set_id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_set_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_set_with_binding.py">PolicySetWithBinding</a></code>
- <code title="get /zones/{zone_id}/policy-sets">client.zones.policy_sets.<a href="./src/keycardai_api/resources/zones/policy_sets/policy_sets.py">list</a>(zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_set_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_set_list_response.py">PolicySetListResponse</a></code>
- <code title="delete /zones/{zone_id}/policy-sets/{policy_set_id}">client.zones.policy_sets.<a href="./src/keycardai_api/resources/zones/policy_sets/policy_sets.py">archive</a>(policy_set_id, \*, zone_id) -> <a href="./src/keycardai_api/types/zones/policy_set_with_binding.py">PolicySetWithBinding</a></code>

### Versions

Types:

```python
from keycardai_api.types.zones.policy_sets import (
    PolicySetVersion,
    VersionListResponse,
    VersionListPoliciesResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/policy-sets/{policy_set_id}/versions">client.zones.policy_sets.versions.<a href="./src/keycardai_api/resources/zones/policy_sets/versions.py">create</a>(policy_set_id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_sets/version_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_sets/policy_set_version.py">PolicySetVersion</a></code>
- <code title="get /zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}">client.zones.policy_sets.versions.<a href="./src/keycardai_api/resources/zones/policy_sets/versions.py">retrieve</a>(version_id, \*, zone_id, policy_set_id) -> <a href="./src/keycardai_api/types/zones/policy_sets/policy_set_version.py">PolicySetVersion</a></code>
- <code title="patch /zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}">client.zones.policy_sets.versions.<a href="./src/keycardai_api/resources/zones/policy_sets/versions.py">update</a>(version_id, \*, zone_id, policy_set_id, \*\*<a href="src/keycardai_api/types/zones/policy_sets/version_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_sets/policy_set_version.py">PolicySetVersion</a></code>
- <code title="get /zones/{zone_id}/policy-sets/{policy_set_id}/versions">client.zones.policy_sets.versions.<a href="./src/keycardai_api/resources/zones/policy_sets/versions.py">list</a>(policy_set_id, \*, zone_id, \*\*<a href="src/keycardai_api/types/zones/policy_sets/version_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_sets/version_list_response.py">VersionListResponse</a></code>
- <code title="delete /zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}">client.zones.policy_sets.versions.<a href="./src/keycardai_api/resources/zones/policy_sets/versions.py">archive</a>(version_id, \*, zone_id, policy_set_id) -> <a href="./src/keycardai_api/types/zones/policy_sets/policy_set_version.py">PolicySetVersion</a></code>
- <code title="get /zones/{zone_id}/policy-sets/{policy_set_id}/versions/{version_id}/policies">client.zones.policy_sets.versions.<a href="./src/keycardai_api/resources/zones/policy_sets/versions.py">list_policies</a>(version_id, \*, zone_id, policy_set_id, \*\*<a href="src/keycardai_api/types/zones/policy_sets/version_list_policies_params.py">params</a>) -> <a href="./src/keycardai_api/types/zones/policy_sets/version_list_policies_response.py">VersionListPoliciesResponse</a></code>

# Organizations

Types:

```python
from keycardai_api.types import (
    Organization,
    PageInfoCursor,
    RoleScope,
    TokenResponse,
    OrganizationListResponse,
    OrganizationListIdentitiesResponse,
    OrganizationListRolesResponse,
)
```

Methods:

- <code title="post /organizations">client.organizations.<a href="./src/keycardai_api/resources/organizations/organizations.py">create</a>(\*\*<a href="src/keycardai_api/types/organization_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/organization.py">Organization</a></code>
- <code title="get /organizations/{organization_id}">client.organizations.<a href="./src/keycardai_api/resources/organizations/organizations.py">retrieve</a>(organization_id, \*\*<a href="src/keycardai_api/types/organization_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/organization.py">Organization</a></code>
- <code title="patch /organizations/{organization_id}">client.organizations.<a href="./src/keycardai_api/resources/organizations/organizations.py">update</a>(organization_id, \*\*<a href="src/keycardai_api/types/organization_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/organization.py">Organization</a></code>
- <code title="get /organizations">client.organizations.<a href="./src/keycardai_api/resources/organizations/organizations.py">list</a>(\*\*<a href="src/keycardai_api/types/organization_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="post /organizations/{organization_id}/token">client.organizations.<a href="./src/keycardai_api/resources/organizations/organizations.py">exchange_token</a>(organization_id) -> <a href="./src/keycardai_api/types/token_response.py">TokenResponse</a></code>
- <code title="get /organizations/{organization_id}/identities">client.organizations.<a href="./src/keycardai_api/resources/organizations/organizations.py">list_identities</a>(organization_id, \*\*<a href="src/keycardai_api/types/organization_list_identities_params.py">params</a>) -> <a href="./src/keycardai_api/types/organization_list_identities_response.py">OrganizationListIdentitiesResponse</a></code>
- <code title="get /organizations/{organization_id}/roles">client.organizations.<a href="./src/keycardai_api/resources/organizations/organizations.py">list_roles</a>(organization_id, \*\*<a href="src/keycardai_api/types/organization_list_roles_params.py">params</a>) -> <a href="./src/keycardai_api/types/organization_list_roles_response.py">OrganizationListRolesResponse</a></code>

## Users

Types:

```python
from keycardai_api.types.organizations import (
    OrganizationRole,
    OrganizationStatus,
    OrganizationUser,
    UserListResponse,
)
```

Methods:

- <code title="get /organizations/{organization_id}/users/{user_id}">client.organizations.users.<a href="./src/keycardai_api/resources/organizations/users.py">retrieve</a>(user_id, \*, organization_id, \*\*<a href="src/keycardai_api/types/organizations/user_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/organization_user.py">OrganizationUser</a></code>
- <code title="patch /organizations/{organization_id}/users/{user_id}">client.organizations.users.<a href="./src/keycardai_api/resources/organizations/users.py">update</a>(user_id, \*, organization_id, \*\*<a href="src/keycardai_api/types/organizations/user_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/organization_user.py">OrganizationUser</a></code>
- <code title="get /organizations/{organization_id}/users">client.organizations.users.<a href="./src/keycardai_api/resources/organizations/users.py">list</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/user_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/user_list_response.py">UserListResponse</a></code>
- <code title="delete /organizations/{organization_id}/users/{user_id}">client.organizations.users.<a href="./src/keycardai_api/resources/organizations/users.py">delete</a>(user_id, \*, organization_id) -> None</code>

## Invitations

Types:

```python
from keycardai_api.types.organizations import Invitation, InvitationStatus, InvitationListResponse
```

Methods:

- <code title="post /organizations/{organization_id}/invitations">client.organizations.invitations.<a href="./src/keycardai_api/resources/organizations/invitations.py">create</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/invitation_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/invitation.py">Invitation</a></code>
- <code title="get /organizations/{organization_id}/invitations">client.organizations.invitations.<a href="./src/keycardai_api/resources/organizations/invitations.py">list</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/invitation_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/invitation_list_response.py">InvitationListResponse</a></code>
- <code title="delete /organizations/{organization_id}/invitations/{invitation_id}">client.organizations.invitations.<a href="./src/keycardai_api/resources/organizations/invitations.py">delete</a>(invitation_id, \*, organization_id) -> None</code>

## ServiceAccounts

Types:

```python
from keycardai_api.types.organizations import ServiceAccount, ServiceAccountListResponse
```

Methods:

- <code title="post /organizations/{organization_id}/service-accounts">client.organizations.service_accounts.<a href="./src/keycardai_api/resources/organizations/service_accounts/service_accounts.py">create</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/service_account_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_account.py">ServiceAccount</a></code>
- <code title="get /organizations/{organization_id}/service-accounts/{service_account_id}">client.organizations.service_accounts.<a href="./src/keycardai_api/resources/organizations/service_accounts/service_accounts.py">retrieve</a>(service_account_id, \*, organization_id, \*\*<a href="src/keycardai_api/types/organizations/service_account_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_account.py">ServiceAccount</a></code>
- <code title="patch /organizations/{organization_id}/service-accounts/{service_account_id}">client.organizations.service_accounts.<a href="./src/keycardai_api/resources/organizations/service_accounts/service_accounts.py">update</a>(service_account_id, \*, organization_id, \*\*<a href="src/keycardai_api/types/organizations/service_account_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_account.py">ServiceAccount</a></code>
- <code title="get /organizations/{organization_id}/service-accounts">client.organizations.service_accounts.<a href="./src/keycardai_api/resources/organizations/service_accounts/service_accounts.py">list</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/service_account_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_account_list_response.py">ServiceAccountListResponse</a></code>
- <code title="delete /organizations/{organization_id}/service-accounts/{service_account_id}">client.organizations.service_accounts.<a href="./src/keycardai_api/resources/organizations/service_accounts/service_accounts.py">delete</a>(service_account_id, \*, organization_id) -> None</code>

### Credentials

Types:

```python
from keycardai_api.types.organizations.service_accounts import (
    ServiceAccountCredential,
    CredentialCreateResponse,
    CredentialListResponse,
)
```

Methods:

- <code title="post /organizations/{organization_id}/service-accounts/{service_account_id}/credentials">client.organizations.service_accounts.credentials.<a href="./src/keycardai_api/resources/organizations/service_accounts/credentials.py">create</a>(service_account_id, \*, organization_id, \*\*<a href="src/keycardai_api/types/organizations/service_accounts/credential_create_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_accounts/credential_create_response.py">CredentialCreateResponse</a></code>
- <code title="get /organizations/{organization_id}/service-accounts/{service_account_id}/credentials/{credential_id}">client.organizations.service_accounts.credentials.<a href="./src/keycardai_api/resources/organizations/service_accounts/credentials.py">retrieve</a>(credential_id, \*, organization_id, service_account_id, \*\*<a href="src/keycardai_api/types/organizations/service_accounts/credential_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_accounts/service_account_credential.py">ServiceAccountCredential</a></code>
- <code title="patch /organizations/{organization_id}/service-accounts/{service_account_id}/credentials/{credential_id}">client.organizations.service_accounts.credentials.<a href="./src/keycardai_api/resources/organizations/service_accounts/credentials.py">update</a>(credential_id, \*, organization_id, service_account_id, \*\*<a href="src/keycardai_api/types/organizations/service_accounts/credential_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_accounts/service_account_credential.py">ServiceAccountCredential</a></code>
- <code title="get /organizations/{organization_id}/service-accounts/{service_account_id}/credentials">client.organizations.service_accounts.credentials.<a href="./src/keycardai_api/resources/organizations/service_accounts/credentials.py">list</a>(service_account_id, \*, organization_id, \*\*<a href="src/keycardai_api/types/organizations/service_accounts/credential_list_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/service_accounts/credential_list_response.py">CredentialListResponse</a></code>
- <code title="delete /organizations/{organization_id}/service-accounts/{service_account_id}/credentials/{credential_id}">client.organizations.service_accounts.credentials.<a href="./src/keycardai_api/resources/organizations/service_accounts/credentials.py">delete</a>(credential_id, \*, organization_id, service_account_id) -> None</code>

## SSOConnection

Types:

```python
from keycardai_api.types.organizations import SSOConnection, SSOConnectionProtocol
```

Methods:

- <code title="get /organizations/{organization_id}/sso-connection">client.organizations.sso_connection.<a href="./src/keycardai_api/resources/organizations/sso_connection.py">retrieve</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/sso_connection_retrieve_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/sso_connection.py">SSOConnection</a></code>
- <code title="patch /organizations/{organization_id}/sso-connection">client.organizations.sso_connection.<a href="./src/keycardai_api/resources/organizations/sso_connection.py">update</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/sso_connection_update_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/sso_connection.py">SSOConnection</a></code>
- <code title="delete /organizations/{organization_id}/sso-connection">client.organizations.sso_connection.<a href="./src/keycardai_api/resources/organizations/sso_connection.py">disable</a>(organization_id) -> None</code>
- <code title="post /organizations/{organization_id}/sso-connection">client.organizations.sso_connection.<a href="./src/keycardai_api/resources/organizations/sso_connection.py">enable</a>(organization_id, \*\*<a href="src/keycardai_api/types/organizations/sso_connection_enable_params.py">params</a>) -> <a href="./src/keycardai_api/types/organizations/sso_connection.py">SSOConnection</a></code>

# Invitations

Types:

```python
from keycardai_api.types import InvitationRetrieveResponse, InvitationAcceptResponse
```

Methods:

- <code title="get /invitations/{token}">client.invitations.<a href="./src/keycardai_api/resources/invitations.py">retrieve</a>(token) -> <a href="./src/keycardai_api/types/invitation_retrieve_response.py">InvitationRetrieveResponse</a></code>
- <code title="post /invitations/{token}/accept">client.invitations.<a href="./src/keycardai_api/resources/invitations.py">accept</a>(token) -> <a href="./src/keycardai_api/types/invitation_accept_response.py">InvitationAcceptResponse</a></code>

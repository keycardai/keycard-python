# Changelog

## 0.17.0 (2026-08-26)

Full Changelog: [v0.16.0...v0.17.0](https://github.com/keycardai/keycard-python/compare/v0.16.0...v0.17.0)

### ⚠ BREAKING CHANGES

* retire POST /organizations/{id}/token

### Features

* **ACC-709:** application assignees + expose role assignments ([6a76dbf](https://github.com/keycardai/keycard-python/commit/6a76dbf04cbd9d16c1054a262a7a42a01668f035))
* add external_id_claim to provider openid protocol ([9ea5e49](https://github.com/keycardai/keycard-python/commit/9ea5e498695a9f88991515aa306f3b045711d0e4))
* **applications:** allow unified-gateway and mcp-server traits (ECO-128) ([414ac68](https://github.com/keycardai/keycard-python/commit/414ac68a77bb5c54837b7d4146c2e8b8735f6370))
* **CX-782:** paginate + search application dependencies ([02e6bde](https://github.com/keycardai/keycard-python/commit/02e6bdef7ec3aa0c3313b12f1dc814510c83c773))
* **CX-860:** paginate application provided-resources endpoint ([aac9e86](https://github.com/keycardai/keycard-python/commit/aac9e86b2a4801ae35fc773b4cc1fd0748becf06))
* **CX-862:** remove legacy traits[]/traits[all] aliases ([23984b7](https://github.com/keycardai/keycard-python/commit/23984b713fb45653d6a09e8eb2b88a679ef8a7ae))
* filter users by identifier in management list ([147af02](https://github.com/keycardai/keycard-python/commit/147af020e8e8c31678928137fb85386b54dd4ec6))
* **ID-365:** support additional SSO provider configuration options ([526b229](https://github.com/keycardai/keycard-python/commit/526b22958acc91a11569ba3f8453a004eb03f6f5))
* **ID-456:** groups API create + get ([976fbbd](https://github.com/keycardai/keycard-python/commit/976fbbd318ab99629796bc28ddf2dc0dcfad562e))
* **ID-478:** zones.external_sync_enabled column and update API ([fd4134c](https://github.com/keycardai/keycard-python/commit/fd4134c71676e377b1acc47dbb197a6b437a9697))
* **ID-480:** external_sync_tokens table and management APIs ([0e04c06](https://github.com/keycardai/keycard-python/commit/0e04c066c57f96bef597416d4a4a1f77ec6c43fc))
* **providers:** add filter[id] to list endpoint (ID-547) ([20da67a](https://github.com/keycardai/keycard-python/commit/20da67a5559d2188a4b127f6d30ce3ae43e20751))
* **providers:** store brand icon_url in provider metadata ([f298c38](https://github.com/keycardai/keycard-python/commit/f298c382bdbe7e68b8a1556f36fe466b6155a5a8))
* **resources:** add filter[owner_type] to the resource list (ECO-225) ([ede883a](https://github.com/keycardai/keycard-python/commit/ede883a754b07dfd8beff31afd57860d8d65814b))
* **resources:** add search, sort, and filter[id] to the paginated resource list ([ca1681d](https://github.com/keycardai/keycard-python/commit/ca1681d46b70bd5e2913a4a8906793bc55c34ca7))
* **resources:** filter the resource list by trait ([6cab4f0](https://github.com/keycardai/keycard-python/commit/6cab4f0985ac778837b272353cf1f729b88bd9d9))
* retire POST /organizations/{id}/token ([8a65582](https://github.com/keycardai/keycard-python/commit/8a65582d81e48738200067e7e8ca7ec02590563c))
* **sdk:** expose zone roles, groups, and role assignments in Stainless config ([45970b1](https://github.com/keycardai/keycard-python/commit/45970b10df4451e04810706fba32366153487896))
* **sdk:** generate a client for the existing /policy/bundle endpoint ([518c473](https://github.com/keycardai/keycard-python/commit/518c473dcb23f0d68e849838a070187addf422a9))
* **stlc:** configurable CI runner and private-production-repo support in workflow templates ([1c22f7e](https://github.com/keycardai/keycard-python/commit/1c22f7ea4ae904c4864a794dc4aaa46afa7d7e0e))


### Bug Fixes

* **ACC-613:** preserve source order of policies in draft/convert cedar_json ([6d27d21](https://github.com/keycardai/keycard-python/commit/6d27d213ac66fb9f1890409a380924c3edb44b99))
* **ci:** resolve Stainless error diagnostics and enforce fail_on: error ([8a01934](https://github.com/keycardai/keycard-python/commit/8a01934b6ceb8636db998f0498d86ccb810cf639))
* **deps:** close critical Dependabot alerts ([fe31508](https://github.com/keycardai/keycard-python/commit/fe315084c22655d49d199b33a0cb16c17e4bbbb1))
* exact-match identifier filter on resources management list ([846f24e](https://github.com/keycardai/keycard-python/commit/846f24efdb2492e4ea0741167ebc7153af5d0d1e))
* **ID-448:** keyset cursor drops same-millisecond rows (precision mismatch) ([dad9ddb](https://github.com/keycardai/keycard-python/commit/dad9ddb0165f422ef1d05d851d4fdf912ee1d43b))
* **internal:** resolve build failures ([15cb317](https://github.com/keycardai/keycard-python/commit/15cb317c1d1ea8462b30bff1411e52a554df0fb0))
* **sdk:** generate /policy/bundle body as raw binary, not multipart ([d516a7f](https://github.com/keycardai/keycard-python/commit/d516a7f7b207aa4eed33d1a401721b9aa1ecd5d9))


### Chores

* de-dup and align types across API specs ([bf16103](https://github.com/keycardai/keycard-python/commit/bf161039858f079eabd6abf9102fa439633b9bc9))
* Fixes found during Terraform work ([8389f30](https://github.com/keycardai/keycard-python/commit/8389f304ffae7c4bbe512de541a6896469be273f))

## 0.16.0 (2026-06-30)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/keycardai/keycard-python/compare/v0.15.0...v0.16.0)

### Features

* **ID-328:** add single_logout_enabled provider config ([1f22fa5](https://github.com/keycardai/keycard-python/commit/1f22fa59bd49ec2b1368c8b1e58c6c7bd14e1bcc))


### Bug Fixes

* align create/update schema validations ([dae89df](https://github.com/keycardai/keycard-python/commit/dae89dfbb053ae43a3fdfb46ea7087b890b46c91))

## 0.15.0 (2026-06-16)

Full Changelog: [v0.14.0...v0.15.0](https://github.com/keycardai/keycard-python/compare/v0.14.0...v0.15.0)

### Features

* **ACC-513:** reduced scope implementation ([61b9ac2](https://github.com/keycardai/keycard-python/commit/61b9ac28ba47d34bfac883fe6c4af855b92b4eec))
* **ID-185:** Disable Zone Users ([79035f1](https://github.com/keycardai/keycard-python/commit/79035f19f162c3a9823899506f3e2ef2f55be21e))


### Bug Fixes

* Hide non-GA Catalog endpoints from docs and SDKs ([f8023d4](https://github.com/keycardai/keycard-python/commit/f8023d48db9c6f8fc19da8a5ae980f1349436777))
* mark package get x-internal ([bed75a5](https://github.com/keycardai/keycard-python/commit/bed75a5d5eacfeda46141aede9684df4591cda08))

## 0.14.0 (2026-06-09)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/keycardai/keycard-python/compare/v0.13.0...v0.14.0)

### Features

* **ACC-441:** add roles and role assignments to the management api ([9f5a1e7](https://github.com/keycardai/keycard-python/commit/9f5a1e774de8e64d5017806edcfbfc20bfa210b5))
* **iam:** ACC-441 add management api role and assignment routes ([35dbd25](https://github.com/keycardai/keycard-python/commit/35dbd25dacaa358307a45a6d0fb4ebda8d959c0d))
* **ID-269:** Add owner_type: platform | customer to zones ([64d5739](https://github.com/keycardai/keycard-python/commit/64d5739bb4fbc830d6385bc5732c3487ffa8c9fd))
* **ID-270:** gate owner_type and federation.keycard to platform-owned entities ([9e181ce](https://github.com/keycardai/keycard-python/commit/9e181ce9fe1882dd8c0575393ccda5cc02014ef3))

## 0.13.0 (2026-05-28)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/keycardai/keycard-python/compare/v0.12.0...v0.13.0)

### Features

* add openapi tags ([b454ce8](https://github.com/keycardai/keycard-python/commit/b454ce82a14b7e10cd7eb6e4192959a95bba6804))
* add svc-catalog resources to Stainless SDK config ([a94205e](https://github.com/keycardai/keycard-python/commit/a94205e53a7655b33ff7094192c3cf4558cb3a7c))
* **ID-229:** paginate listApplications behind application-pagination flag ([7720da4](https://github.com/keycardai/keycard-python/commit/7720da4f8faf0eca78049dc3d9647f0aa0af6651))

## 0.12.0 (2026-05-21)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/keycardai/keycard-python/compare/v0.11.0...v0.12.0)

### Features

* add scopes to provider openid protocol schemas (ACC-354) ([350683d](https://github.com/keycardai/keycard-python/commit/350683d62f6d36e181f69effb96cd4a6354853db))

## 0.11.0 (2026-05-15)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/keycardai/keycard-python/compare/v0.10.0...v0.11.0)

### Features

* **ACC-277:** list policy versions pinned by a policy-set draft ([1098f3d](https://github.com/keycardai/keycard-python/commit/1098f3dc1da65c5ecc00c7e132bd8c7b8e8bc4fc))
* accept ID Zone platform principals in management API ([1e3311e](https://github.com/keycardai/keycard-python/commit/1e3311ed7a826618f9fe8a34c438e9cea81d5636))
* add jwt_lifetime_seconds to resources ([090a5cd](https://github.com/keycardai/keycard-python/commit/090a5cd8c0f02bc29b29a74b525924fff94320a7))


### Bug Fixes

* housekeeping ([744a2af](https://github.com/keycardai/keycard-python/commit/744a2afd2465cc5c67ee665636f89675d0913192))

## 0.10.0 (2026-05-11)

Full Changelog: [v0.9.1...v0.10.0](https://github.com/keycardai/keycard-python/compare/v0.9.1...v0.10.0)

### Features

* **ID-177:** make invitations.last_sent_at non-nullable ([46ec164](https://github.com/keycardai/keycard-python/commit/46ec164a1a5fac42abb7cc0f64ef5f1855002a64))
* **internal/types:** support eagerly validating pydantic iterators ([4ccb8f5](https://github.com/keycardai/keycard-python/commit/4ccb8f5c0c4be16d9394dba8e62425ed1b89232c))

## 0.9.1 (2026-05-08)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/keycardai/keycard-python/compare/v0.9.0...v0.9.1)

### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([74bca73](https://github.com/keycardai/keycard-python/commit/74bca7339a86bcc9f44c609e7ae15d35ed1b1a25))

## 0.9.0 (2026-05-07)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/keycardai/keycard-python/compare/v0.8.0...v0.9.0)

### Features

* **ACC-255:** active-first sort on listPolicySets (multi-key sort MVP) ([987a8ad](https://github.com/keycardai/keycard-python/commit/987a8ad21069fbeb6e6b27d99cf8d2046da95e16))

## 0.8.0 (2026-05-06)

Full Changelog: [v0.7.1...v0.8.0](https://github.com/keycardai/keycard-python/compare/v0.7.1...v0.8.0)

### Features

* **mgmt api:** cursor pagination works with sort on listInvitations ([e7960e5](https://github.com/keycardai/keycard-python/commit/e7960e5a9b3fa4861ef1c9772ec55bf51f9aefa4))

## 0.7.1 (2026-04-30)

Full Changelog: [v0.7.0...v0.7.1](https://github.com/keycardai/keycard-python/compare/v0.7.0...v0.7.1)

### Chores

* **internal:** reformat pyproject.toml ([3ff89f0](https://github.com/keycardai/keycard-python/commit/3ff89f0097cb8b89b683dd94439709887dcbd933))

## 0.7.0 (2026-04-30)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/keycardai/keycard-python/compare/v0.6.0...v0.7.0)

### Features

* **ACC-225:** return both cedar_json and cedar_raw on policy version fetch ([771b574](https://github.com/keycardai/keycard-python/commit/771b574e0c53d01dfa0bd216fd88bbdf60b334ab))
* **api:** add latest_schema_version to the Policy entity (ACC-251) ([d423839](https://github.com/keycardai/keycard-python/commit/d4238396da9877ca03f5c9fa486fd72cac72c02c))

## 0.6.0 (2026-04-27)

Full Changelog: [v0.5.1...v0.6.0](https://github.com/keycardai/keycard-python/compare/v0.5.1...v0.6.0)

### Features

* support setting headers via env ([326b60f](https://github.com/keycardai/keycard-python/commit/326b60ffdea016d200f4cac53df6459e9d4b60fe))

## 0.5.1 (2026-04-27)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/keycardai/keycard-python/compare/v0.5.0...v0.5.1)

### Bug Fixes

* use correct field name format for multipart file arrays ([046e324](https://github.com/keycardai/keycard-python/commit/046e3246746af81aa20f09687680b79112447386))

## 0.5.0 (2026-04-24)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/keycardai/keycard-python/compare/v0.4.0...v0.5.0)

### Features

* add filter/query to policy (set) queries (ACC-147) ([48e4c98](https://github.com/keycardai/keycard-python/commit/48e4c98c14f04e506f5d0698b0d4b9be213c34a3))
* add standard pagination/filter/search definitions ([74568ba](https://github.com/keycardai/keycard-python/commit/74568baea477a4c8a327b7cc3b515cde725844ee))
* Matte/revert in progress commits ([23d8ad1](https://github.com/keycardai/keycard-python/commit/23d8ad1831d6af7b58c270f71eba88dba8c04511))
* **mgmt api:** add list Users pagination, querying, filtering ([0cfa763](https://github.com/keycardai/keycard-python/commit/0cfa7635cdf53f1f6260be874bb830dc55086082))
* resource prefix flag ([74c685b](https://github.com/keycardai/keycard-python/commit/74c685b402d9c0f295705b53a99c4a04e88164d3))
* store all evaluation requests for replay and impact (ACC-134) ([46dab9e](https://github.com/keycardai/keycard-python/commit/46dab9e464d05165f6ea5b8380d457b42cdb5feb))


### Bug Fixes

* **deps:** patch vulnerabilities socket found ([#5](https://github.com/keycardai/keycard-python/issues/5)) ([d72befc](https://github.com/keycardai/keycard-python/commit/d72befc3ea53f9b0eec052bb447b5f64d975fb8a))


### Chores

* **internal:** more robust bootstrap script ([3fc374c](https://github.com/keycardai/keycard-python/commit/3fc374c40178b097786b0b2e6d0b6387fd5152f9))

## 0.4.0 (2026-04-17)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/keycardai/keycard-python/compare/v0.3.0...v0.4.0)

### Features

* add email search to list organization identities endpoint ([f9b2707](https://github.com/keycardai/keycard-python/commit/f9b2707b0649678407423d2f5b3007a6d7bcc2e6))
* add openapi-yaml command ([b37854a](https://github.com/keycardai/keycard-python/commit/b37854a0910db1c34df7509b706c34306a160ebf))
* add owner_type and enforce protection for platform-owned versions (ACC-29) ([bfac76d](https://github.com/keycardai/keycard-python/commit/bfac76da47db6264d00d9df73c387a8e5e175840))
* add PRM discovery to MCP gateway endpoint ([fbc502d](https://github.com/keycardai/keycard-python/commit/fbc502dc075d7a0f6890317fc59203ca51d644a7))
* improved identities pagination ([d4c4d1b](https://github.com/keycardai/keycard-python/commit/d4c4d1ba4d76d709e6067d36f1848d293d227a81))
* **internal:** implement indices array format for query and form serialization ([617099d](https://github.com/keycardai/keycard-python/commit/617099df6ed00538530a5f4ed285130dd5ac13c7))
* normalize and validate user input (ACC-107) ([7bb7c97](https://github.com/keycardai/keycard-python/commit/7bb7c970e37b50353c54b4afc6307608c5bcdd94))
* provide more context for policy schema ([46bea8a](https://github.com/keycardai/keycard-python/commit/46bea8a4493318b0b37904119e057cb7b4e50550))
* shadow testing (ACC-14) ([f8f9ac8](https://github.com/keycardai/keycard-python/commit/f8f9ac8089531b5613cb9147dd736de348de2d33))
* Support for user identifier and provider user identifier claim ([ac47cc2](https://github.com/keycardai/keycard-python/commit/ac47cc20c48168e226a78d5402d7f8e745881bb8))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([3a94db2](https://github.com/keycardai/keycard-python/commit/3a94db26d731d5d0a34957d0aec691b0346eb275))
* ensure file data are only sent as 1 parameter ([bcc62f9](https://github.com/keycardai/keycard-python/commit/bcc62f9c4cd18748dc5a26eb4d84fee22573a237))
* sanitize endpoint path params ([6993e56](https://github.com/keycardai/keycard-python/commit/6993e56d5e9a79713471a0b2b33920c1e2da77d9))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([2b5cca8](https://github.com/keycardai/keycard-python/commit/2b5cca867abc3dd0171c465ec056bfff88cd8f81))


### Chores

* **ci:** skip lint on metadata-only changes ([bc52e3f](https://github.com/keycardai/keycard-python/commit/bc52e3f59616d0754b7f0bc30374fac7f357f63b))
* **internal:** update gitignore ([24f9a15](https://github.com/keycardai/keycard-python/commit/24f9a15a6031769c2a5912a3eda480fb82fc17b1))

## 0.3.0 (2026-03-16)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/keycardai/keycard-python/compare/v0.2.0...v0.3.0)

### Features

* use common bearerAuth and OAuth2 security schemes ([367a8c2](https://github.com/keycardai/keycard-python/commit/367a8c261a1d7a289a092949da25e6da04cd16f3))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([8d6df39](https://github.com/keycardai/keycard-python/commit/8d6df397c7b9a5c176b599ca6e012400ff452fdf))
* **pydantic:** do not pass `by_alias` unless set ([2a6ae9b](https://github.com/keycardai/keycard-python/commit/2a6ae9bc20c6c3a2b483613799cc16001a495d0d))


### Chores

* configure new SDK language ([37fcdc3](https://github.com/keycardai/keycard-python/commit/37fcdc3d805b5a0c0f449a3c45ad27dedb8e5ea0))
* **internal:** tweak CI branches ([e58ab99](https://github.com/keycardai/keycard-python/commit/e58ab9952115c67eb8614bd4c441ee9426f5364e))

## 0.2.0 (2026-03-16)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/keycardai/keycard-python/compare/v0.1.0...v0.2.0)

### Features

* add OAuth2 as alternative auth on management API endpoints ([52c6c27](https://github.com/keycardai/keycard-python/commit/52c6c27bb85b2f07f5ead2490ab902fef4816dca))
* add OAuth2 client credentials security scheme from common spec ([be3f5df](https://github.com/keycardai/keycard-python/commit/be3f5df50f9f6434ab8836c06adeda99c9f514d4))
* add OAuth2 client_credentials auth to SDK config ([40d6e7a](https://github.com/keycardai/keycard-python/commit/40d6e7a713f518df3653430ed7cee25b2db79140))
* Include `array_format: brackets` settings ([59f0159](https://github.com/keycardai/keycard-python/commit/59f0159a9a84d4a89b219faf4e7ac67556c22392))
* PyPi underscore package name ([3cd5a1e](https://github.com/keycardai/keycard-python/commit/3cd5a1e6bd8684f86efb5d77249cd950848631fe))
* support HTTP Basic Auth for service account token endpoint (RFC 6749 2.3.1) ([b9d6db0](https://github.com/keycardai/keycard-python/commit/b9d6db00b5388ae7b8872c6f5f4345cb132edb56))
* update pkg-oapi-common and add OAuth2 security scheme ([4a94884](https://github.com/keycardai/keycard-python/commit/4a9488474597b923dac403292e207ba0d8487754))


### Bug Fixes

* **tests:** correct setup of OAuth 2 Client Credentials tests ([fe2b8ba](https://github.com/keycardai/keycard-python/commit/fe2b8ba8b7867cc86942b5306bb8cb31f5d469ac))


### Chores

* hide unstable mcp features from api documentation ([0fd55ba](https://github.com/keycardai/keycard-python/commit/0fd55ba2f11a5ad75e6c13702a060853a209156c))


### Documentation

* remove MCP endpoints ([06fb1fd](https://github.com/keycardai/keycard-python/commit/06fb1fdec007a642eac2debbc11acdef112635c1))

## 0.1.0 (2026-03-10)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/keycardai/keycard-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([35cda8b](https://github.com/keycardai/keycard-python/commit/35cda8ba3ab78e3b108db05ddc08063b2f030825))
* configure SDK packages ([ad84bcc](https://github.com/keycardai/keycard-python/commit/ad84bcc0fde279929c6a472ec46ca449dd454461))
* consolidate prefixed security schemes into canonical names ([940549a](https://github.com/keycardai/keycard-python/commit/940549a26f6782c3ffe174f68196320b26b9fee4))
* jelmer/stainless keycardai configuration ([d84041a](https://github.com/keycardai/keycard-python/commit/d84041a5cb62b5480da8a3ef6f007c64c89b924f))
* remove unused security schemes from joined spec ([95aa9f5](https://github.com/keycardai/keycard-python/commit/95aa9f57d74798443baf8464e67232d7331030a8))
* Typescript package name @keycardai/api ([abb571d](https://github.com/keycardai/keycard-python/commit/abb571d3f052d0459ef6f5da4a30e491f3c86de3))


### Chores

* sync repo ([c2b5238](https://github.com/keycardai/keycard-python/commit/c2b52387f3f3103620c6f5ee145b8e2da1bf1cb9))
* update SDK settings ([2758508](https://github.com/keycardai/keycard-python/commit/2758508355dd662ba84aa6d56800dbafedf43374))
* update SDK settings ([aaed6c5](https://github.com/keycardai/keycard-python/commit/aaed6c5d438d5924de89990591a6576b917c1409))

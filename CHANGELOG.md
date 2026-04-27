# Changelog

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

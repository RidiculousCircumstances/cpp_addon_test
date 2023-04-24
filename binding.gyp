{
	"targets": [
		{
			"target_name": "addon",
			"sources": ["addon.cpp"],
			'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
			'cflags!': ['-fno-exceptions'],
			'cflags_cc!': ['-fno-exceptions'],
			'conditions': [
				["OS=='win'", {
					"defines": [
						"_HAS_EXCEPTIONS=1"
					],
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1
						},
					},
				}],
			]
		}
	]
}
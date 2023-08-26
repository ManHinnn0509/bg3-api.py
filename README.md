# bg3-api.py

An API for BG3 modding (Custom items), I don't think this project can help on 3D modding

This project's size is around `288~340 MB` because I included the `lsx` files

**I can't guarantee this project is good cause I'm new to FastAPI and I only used it on browser (Clicking the links only)**

## The .env file

~~Yes I included it too because it's like a setting file in here, no personal infos etc, I might change it to a Python file in the future~~

You can create a `.env` file with following template:

```
API_SECRET=

HOST_ADDRESS=
HOST_PORT=

ENABLE_AUTH=
CASE_SENSITIVE=
```

Set `ENABLE_AUTH` to `True` to enable API key ([auth.py](auth.py)), it's disabled by default

Set `CASE_SENSITIVE` to `True` to enable case sensitive (Disabled by default)

## Endpoints and descriptions

You can get the description and URL of each endpoint with a GET request to the index

## Example

Let's say that I want to find the item data of a ring called `A Sparking Promise` ([wiki here](https://baldursgate3.wiki.fextralife.com/A+Sparking+Promise))

I will send a GET request to `/findHandle` with query `?equals=A%20Sparking%20Promise`

This will be returned:

```json
{
  "h826192c0g098fg4224gb0d3g5fa7b8cecd3f": {
    "text": "A Sparking Promise",
    "version": 2,
    "url": "http://127.0.0.1:1053/findByHandle?handle=h826192c0g098fg4224gb0d3g5fa7b8cecd3f"
  }
}
```

Use the "url" returned to get more info, this will be returned from it:

```json
{
  "Gustav/Public/GustavDev/RootTemplates/": {
    "5c8235c3-1aad-4b6d-bd0c-9753c77da5d2": {
      "lsx": "http://127.0.0.1:1053/getLsx?mapKey=5c8235c3-1aad-4b6d-bd0c-9753c77da5d2",
      "txt": "http://127.0.0.1:1053/getTxt?mapKey=5c8235c3-1aad-4b6d-bd0c-9753c77da5d2"
    }
  }
}
```

The response of the `lsx`'s url is a `xml` response, example:

```xml
<save>
    <version major="4" minor="0" revision="9" build="328"/>
    <region id="Templates">
        <node id="Templates">
            <children>
                <node id="GameObjects">
                    <attribute id="MapKey" type="FixedString" value="5c8235c3-1aad-4b6d-bd0c-9753c77da5d2"/>
                    <attribute id="Name" type="LSString" value="MAG_ChargedLightning_EnsnaringShock_Ring"/>
                    <attribute id="LevelName" type="FixedString" value=""/>
                    <attribute id="Type" type="FixedString" value="item"/>
                    <attribute id="ParentTemplateId" type="FixedString" value="52f6619c-edd3-4493-a420-c124f52c2a03"/>
                    <attribute id="DisplayName" type="TranslatedString" handle="h826192c0g098fg4224gb0d3g5fa7b8cecd3f" version="2"/>
                    <attribute id="Icon" type="FixedString" value="Item_MAG_ChargedLightning_EnsnaringShock_Ring"/>
                    <attribute id="Stats" type="FixedString" value="MAG_ChargedLightning_EnsnaringShock_Ring"/>
                    <attribute id="Description" type="TranslatedString" handle="hee388d0cga972g4213g983eg61e3042f1e20" version="1"/>
                    <attribute id="TechnicalDescription" type="TranslatedString" handle="" version="0"/>
                </node>
            </children>
        </node>
    </region>
</save>
```

The response of the `txt`'s url is a `json` response with file path & file names with the given `mapKey` in them, example:

```json
{
  "Gustav/Public/GustavDev/Stats/Generated/Data/": {
    "Armor.txt": [
      [
        "new entry \"MAG_ChargedLightning_EnsnaringShock_Ring\"",
        "type \"Armor\"",
        "using \"_Ring_Magic\"",
        "data \"RootTemplate\" \"5c8235c3-1aad-4b6d-bd0c-9753c77da5d2\"",
        "data \"ItemGroup\" \"\"",
        "data \"ValueUUID\" \"94356ef2-bb14-4595-88cf-86f544ef12eb\"",
        "data \"Rarity\" \"Rare\"",
        "data \"Boosts\" \"UnlockSpell(Target_MAG_ChargedLightning_EnsnaringShock)\"",
        "data \"Unique\" \"1\""
      ]
    ]
  }
}
```

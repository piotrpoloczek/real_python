import yaml
import serializers_3


class YamlSerializer(serializers_3.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)

serializers_3.factory.register_format("YAML", YamlSerializer)
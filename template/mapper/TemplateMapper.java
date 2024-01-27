package <package_name>.mapper;

import lombok.AccessLevel;
import lombok.NoArgsConstructor;

import <package_name>.entity.<entity_name_uppercase>;
import <package_name>.model.<entity_name_uppercase>Dto;

@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class <entity_name_uppercase>Mapper {

    public static <entity_name_uppercase>Dto toDto(<entity_name_uppercase> <entity_name_lowercase>) {
        return <entity_name_uppercase>Dto.builder()
                .id(<entity_name_lowercase>.getId())
                // todo mapping
                .build();
    }

    public static <entity_name_uppercase> toCreateEntity(<entity_name_uppercase>Dto <entity_name_lowercase>Dto) {
        return <entity_name_uppercase>.builder()
                .id(<entity_name_lowercase>Dto.id())
                // todo mapping
                .build();
    }

    public static void updateEntity(<entity_name_uppercase> <entity_name_lowercase>, <entity_name_uppercase>Dto <entity_name_lowercase>Dto) {
        // todo entity update
    }
}

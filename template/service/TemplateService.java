package <package_name>.service;

import java.util.Optional;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import <package_name>.entity.<entity_name_uppercase>;
import <package_name>.mapper.<entity_name_uppercase>Mapper;
import <package_name>.model.<entity_name_uppercase>Dto;
import <package_name>.repository.<entity_name_uppercase>Repository;

import static org.springframework.http.HttpStatus.NOT_FOUND;

@Service
@RequiredArgsConstructor
public class <entity_name_uppercase>Service {

    private final <entity_name_uppercase>Repository <entity_name_lowercase>Repository;

    @Transactional
    public <entity_name_uppercase>Dto create<entity_name_uppercase>(<entity_name_uppercase>Dto <entity_name_lowercase>Dto) {
        <entity_name_uppercase> newEntity = <entity_name_uppercase>Mapper.toCreateEntity(<entity_name_lowercase>Dto);
        <entity_name_lowercase>Repository.saveAndFlush(newEntity);
        return <entity_name_uppercase>Mapper.toDto(newEntity);
    }

    @Transactional
    public <entity_name_uppercase>Dto update<entity_name_uppercase>(<entity_name_uppercase>Dto <entity_name_lowercase>Dto) {
        return Optional.ofNullable(<entity_name_lowercase>Dto.id())
                .flatMap(<entity_name_lowercase>Repository::findById)
                .map(<entity_name_lowercase> -> update<entity_name_uppercase>(<entity_name_lowercase>, <entity_name_lowercase>Dto))
                .orElseThrow(() -> new ResponseStatusException(NOT_FOUND));
    }

    public <entity_name_uppercase>Dto update<entity_name_uppercase>(<entity_name_uppercase> <entity_name_lowercase>, <entity_name_uppercase>Dto <entity_name_lowercase>Dto) {
        <entity_name_uppercase>Mapper.updateEntity(<entity_name_lowercase>, <entity_name_lowercase>Dto);
        <entity_name_lowercase>Repository.saveAndFlush(<entity_name_lowercase>);
        return <entity_name_uppercase>Mapper.toDto(<entity_name_lowercase>);
    }

    public <entity_name_uppercase>Dto get<entity_name_uppercase>(Long <entity_name_lowercase>Id) {
        return Optional.ofNullable(<entity_name_lowercase>Id)
                .flatMap(<entity_name_lowercase>Repository::findById)
                .map(<entity_name_uppercase>Mapper::toDto)
                .orElseThrow(() -> new ResponseStatusException(NOT_FOUND));
    }

    public void delete<entity_name_uppercase>(Long <entity_name_lowercase>Id) {
        Optional.ofNullable(<entity_name_lowercase>Id)
                .flatMap(<entity_name_lowercase>Repository::findById)
                .ifPresentOrElse(<entity_name_lowercase>Repository::delete, () -> {
                    throw new ResponseStatusException(NOT_FOUND);
                });
    }
}

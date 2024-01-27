package <package_name>.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import <package_name>.model.<entity_name_uppercase>Dto;
import <package_name>.service.<entity_name_uppercase>Service;

@RestController
@RequiredArgsConstructor
@RequestMapping(<entity_name_uppercase>Controller.PATH)
public class <entity_name_uppercase>Controller {
    public static final String PATH = "/<entity_name_lowercase>";

    private final <entity_name_uppercase>Service <entity_name_lowercase>Service;

    @PostMapping(consumes = MediaType.APPLICATION_JSON_VALUE,
            produces = MediaType.APPLICATION_JSON_VALUE)
    public <entity_name_uppercase>Dto create<entity_name_uppercase>(@RequestBody <entity_name_uppercase>Dto <entity_name_lowercase>Dto) {
        return <entity_name_lowercase>Service.create<entity_name_uppercase>(<entity_name_lowercase>Dto);
    }

    @PutMapping(consumes = MediaType.APPLICATION_JSON_VALUE,
            produces = MediaType.APPLICATION_JSON_VALUE)
    public <entity_name_uppercase>Dto update<entity_name_uppercase>(@RequestBody <entity_name_uppercase>Dto <entity_name_lowercase>Dto) {
        return <entity_name_lowercase>Service.update<entity_name_uppercase>(<entity_name_lowercase>Dto);
    }

    @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public <entity_name_uppercase>Dto get<entity_name_uppercase>(@RequestParam Long <entity_name_lowercase>Id) {
        return <entity_name_lowercase>Service.get<entity_name_uppercase>(<entity_name_lowercase>Id);
    }

    @DeleteMapping
    public void delete<entity_name_uppercase>(@RequestParam Long <entity_name_lowercase>Id) {
        <entity_name_lowercase>Service.delete<entity_name_uppercase>(<entity_name_lowercase>Id);
    }
}

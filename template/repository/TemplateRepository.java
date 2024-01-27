package <package_name>.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import <package_name>.entity.<entity_name_uppercase>;

@Repository
public interface <entity_name_uppercase>Repository extends JpaRepository<<entity_name_uppercase>, Long> {
}

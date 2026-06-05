# language: es
Feature: Módulo de recargas de celular RecargaYa
  Como usuario del sistema RecargaYa
  Quiero recargar saldo en mi celular
  Para disfrutar de los beneficios según el monto y mi plan

  Background:
    Given el sistema de recargas está disponible

  Scenario: Recarga rechazada por monto menor al mínimo permitido
    Given un usuario con plan "normal"
    When solicita una recarga de $999
    Then la recarga es rechazada
    And no se calcula bonificación

  Scenario: Recarga rechazada por monto mayor al máximo permitido
    Given un usuario con plan "normal"
    When solicita una recarga de $50001
    Then la recarga es rechazada
    And no se calcula bonificación

  Scenario: Recarga aceptada sin bonificación para monto mínimo válido
    Given un usuario con plan "normal"
    When solicita una recarga de $1000
    Then la recarga es aceptada
    And la bonificación es del 0%

  Scenario: Usuario PREMIUM recibe 5% adicional sobre bonificación del 25%
    Given un usuario con plan "premium"
    When solicita una recarga de $30000
    Then la recarga es aceptada
    And la bonificación es del 30%

  Scenario: Usuario PREMIUM sin bonificación base no recibe el 5% adicional
    Given un usuario con plan "premium"
    When solicita una recarga de $5000
    Then la recarga es aceptada
    And la bonificación es del 0%

  Scenario Outline: Bonificaciones en valores límite con plan normal
    Given un usuario con plan "normal"
    When solicita una recarga de $<monto>
    Then el resultado es "<resultado>"
    And la bonificación esperada es <bonificacion>%

    Examples:
      | monto | resultado  | bonificacion |
      | 999   | rechazada  | 0            |
      | 1000  | aceptada   | 0            |
      | 9999  | aceptada   | 0            |
      | 10000 | aceptada   | 10           |
      | 29999 | aceptada   | 10           |
      | 30000 | aceptada   | 25           |
      | 50000 | aceptada   | 25           |
      | 50001 | rechazada  | 0            |

  Scenario Outline: Bonificaciones en valores límite con plan premium
    Given un usuario con plan "premium"
    When solicita una recarga de $<monto>
    Then el resultado es "<resultado>"
    And la bonificación esperada es <bonificacion>%

    Examples:
      | monto | resultado  | bonificacion |
      | 999   | rechazada  | 0            |
      | 1000  | aceptada   | 0            |
      | 9999  | aceptada   | 0            |
      | 10000 | aceptada   | 15           |
      | 29999 | aceptada   | 15           |
      | 30000 | aceptada   | 30           |
      | 50000 | aceptada   | 30           |
      | 50001 | rechazada  | 0            |

from typing import List


class Paciente:
    def __init__(self, nome: str, idade: int):
        self._nome = None
        self._idade = None
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Nome do paciente inválido.")
        self._nome = valor.strip()

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, valor: int):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = valor


class Medico:
    def __init__(self, nome: str, crm: str):
        self._nome = None
        self._crm = None
        self.nome = nome
        self.crm = crm

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Nome do médico inválido.")
        self._nome = valor.strip()

    @property
    def crm(self) -> str:
        return self._crm

    @crm.setter
    def crm(self, valor: str):
        if not valor or len(valor.strip()) < 4:
            raise ValueError("CRM inválido.")
        self._crm = valor.strip()


class Medicamento:
    def __init__(self, nome: str, dosagem: str):
        if not nome or not dosagem:
            raise ValueError("Medicamento inválido.")
        self._nome = nome.strip()
        self._dosagem = dosagem.strip()

    @property
    def descricao(self) -> str:
        return f"{self._nome} - {self._dosagem}"


class Consulta:
    def __init__(self, paciente: Paciente, medico: Medico):
        if not isinstance(paciente, Paciente) or not isinstance(medico, Medico):
            raise TypeError("Paciente e Médico devem ser objetos válidos.")
        
        self._paciente = paciente
        self._medico = medico
        self._medicamentos: List[Medicamento] = []

    def adicionar_medicamento(self, medicamento: Medicamento):
        if not isinstance(medicamento, Medicamento):
            raise TypeError("Objeto inválido.")
        self._medicamentos.append(medicamento)

    def gerar_resumo(self) -> str:
        resumo = []
        resumo.append(f"Paciente: {self._paciente.nome} (Idade: {self._paciente.idade})")
        resumo.append(f"Médico: {self._medico.nome} (CRM: {self._medico.crm})")
        resumo.append("Medicamentos prescritos:")

        if not self._medicamentos:
            resumo.append(" - Nenhum medicamento prescrito.")
        else:
            for med in self._medicamentos:
                resumo.append(f" - {med.descricao}")

        return "\n".join(resumo)


# Exemplo de uso (simulação)
if __name__ == "__main__":
    paciente = Paciente("João Silva", 30)
    medico = Medico("Dra. Maria", "12345")

    consulta = Consulta(paciente, medico)

    consulta.adicionar_medicamento(Medicamento("Paracetamol", "500mg"))
    consulta.adicionar_medicamento(Medicamento("Ibuprofeno", "400mg"))

    print(consulta.gerar_resumo())
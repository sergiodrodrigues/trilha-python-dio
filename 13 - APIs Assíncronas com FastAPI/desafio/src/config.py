from pydantic_settings import BaseSettings, SettingsConfigDict

# Definição da classe Settings que herda de BaseSettings.
class Settings(BaseSettings):
    # Configuração do modelo para carregar variáveis de ambiente de um arquivo .env,
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    # Definição das variáveis de ambiente esperadas:
    # - database_url: URL de conexão com o banco de dados (obrigatória).
    # - environment: Ambiente da aplicação (opcional, padrão é "production").
    database_url: str
    environment: str = "production"

# Cria uma instância da classe Settings, que carrega as configurações do .env.
settings = Settings()

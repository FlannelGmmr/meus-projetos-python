{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRBPGbMQ/vPFgVjLkLqGzp"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VaigwUt3uMI-"
      },
      "outputs": [],
      "source": [
        "import sqlite3\n",
        "\n",
        "conexao = sqlite3.connect(\"bloco_notas.db\")\n",
        "cursor = conexao.cursor()\n",
        "\n",
        "cursor.execute(\"\"\"\n",
        "CREATE TABLE IF NOT EXISTS notas (\n",
        "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "    conteudo TEXT NOT NULL\n",
        ")\n",
        "\"\"\")\n",
        "\n",
        "while True:\n",
        "    print(\"\\n1 - Adicionar\")\n",
        "    print(\"2 - Listar\")\n",
        "    print(\"3 - Excluir\")\n",
        "    print(\"4 - Limpar\")\n",
        "    print(\"5 - Sair\")\n",
        "\n",
        "    opcao = input(\"Opção: \")\n",
        "\n",
        "    if opcao == \"1\":\n",
        "        nota = input(\"Nota: \")\n",
        "\n",
        "        if nota.strip():\n",
        "            cursor.execute(\n",
        "                \"INSERT INTO notas (conteudo) VALUES (?)\",\n",
        "                (nota,)\n",
        "            )\n",
        "            conexao.commit()\n",
        "\n",
        "    elif opcao == \"2\":\n",
        "        cursor.execute(\"SELECT * FROM notas\")\n",
        "        notas = cursor.fetchall()\n",
        "\n",
        "        for nota in notas:\n",
        "            print(nota)\n",
        "\n",
        "    elif opcao == \"3\":\n",
        "        id_nota = input(\"ID: \")\n",
        "\n",
        "        if id_nota.isdigit():\n",
        "            cursor.execute(\n",
        "                \"DELETE FROM notas WHERE id = ?\",\n",
        "                (id_nota,)\n",
        "            )\n",
        "            conexao.commit()\n",
        "\n",
        "    elif opcao == \"4\":\n",
        "        cursor.execute(\"DELETE FROM notas\")\n",
        "        conexao.commit()\n",
        "\n",
        "    elif opcao == \"5\":\n",
        "        break\n",
        "\n",
        "conexao.close()"
      ]
    }
  ]
}